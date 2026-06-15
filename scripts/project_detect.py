#!/usr/bin/env python3
"""ViteForge - Project detection script. Detects framework/language/package manager."""

import json, sys, os
from pathlib import Path


def load_package_json(root: str) -> dict:
    p = Path(root) / "package.json"
    if p.exists():
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {}


def detect_framework(pkg: dict) -> list:
    frameworks = {
        "react": ["react", "react-dom"],
        "vue": ["vue"],
        "svelte": ["svelte"],
        "solid": ["solid-js"],
        "preact": ["preact"],
        "angular": ["@angular/core"],
    }
    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
    found = [fw for fw, keys in frameworks.items() if any(k in deps for k in keys)]
    return found if found else ["vanilla"]


def detect_language(pkg: dict, root: str) -> dict:
    has_ts = (Path(root) / "tsconfig.json").exists()
    has_ts_dep = "typescript" in {
        **pkg.get("dependencies", {}),
        **pkg.get("devDependencies", {}),
    }
    return {"typescript": has_ts or has_ts_dep}


def detect_pm(root: str) -> str:
    for pm, lock in [
        ("pnpm", "pnpm-lock.yaml"),
        ("yarn", "yarn.lock"),
        ("bun", "bun.lockb"),
    ]:
        if (Path(root) / lock).exists():
            return pm
    return "npm"


def detect_existing_vite_config(root: str) -> list:
    candidates = [
        "vite.config.ts", "vite.config.js",
        "vite.config.mjs", "vite.config.mts",
    ]
    return [
        {"file": c, "path": str(Path(root) / c)}
        for c in candidates
        if (Path(root) / c).exists()
    ]


def detect_structure(root: str) -> dict:
    rp = Path(root)
    dirs = {
        "has_src": (rp / "src").is_dir(),
        "has_components": (rp / "src" / "components").is_dir(),
        "has_pages": (rp / "src" / "pages").is_dir(),
        "has_lib": (rp / "lib").is_dir(),
        "has_public": (rp / "public").is_dir(),
        "has_env": len(list(rp.glob(".env*"))) > 0,
        "env_files": [f.name for f in rp.glob(".env*")],
    }
    alias = {}
    if dirs["has_src"]:
        alias["@"] = "./src"
    if dirs["has_lib"]:
        alias["@lib"] = "./lib"
    dirs["suggested_alias"] = alias
    return dirs


def detect_build_scripts(pkg: dict) -> dict:
    scripts = pkg.get("scripts", {})
    return {
        "dev": scripts.get("dev", ""),
        "build": scripts.get("build", ""),
        "preview": scripts.get("preview", ""),
    }


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    if not os.path.isdir(root):
        print(json.dumps({"error": f"Not a directory: {root}"}, ensure_ascii=False))
        sys.exit(1)

    pkg = load_package_json(root)
    result = {
        "root": str(Path(root).resolve()),
        "framework": detect_framework(pkg),
        "language": detect_language(pkg, root),
        "package_manager": detect_pm(root),
        "existing_vite_config": detect_existing_vite_config(root),
        "structure": detect_structure(root),
        "build_scripts": detect_build_scripts(pkg),
        "package_name": pkg.get("name", "unknown"),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
