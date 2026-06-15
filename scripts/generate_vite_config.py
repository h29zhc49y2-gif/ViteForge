#!/usr/bin/env python3
"""ViteForge - Generate complete vite.config.ts from project detection."""

import json, sys, os, argparse
from datetime import datetime
from pathlib import Path


PLUGIN_DEPS = {
    "react": {"package": "@vitejs/plugin-react", "import": "import react from '@vitejs/plugin-react'", "usage": "react()"},
    "vue": {"package": "@vitejs/plugin-vue", "import": "import vue from '@vitejs/plugin-vue'", "usage": "vue()"},
    "svelte": {"package": "@sveltejs/vite-plugin-svelte", "import": "import { svelte } from '@sveltejs/vite-plugin-svelte'", "usage": "svelte()"},
    "visualizer": {"package": "rollup-plugin-visualizer", "import": "import { visualizer } from 'rollup-plugin-visualizer'", "usage": "visualizer({ open: true })"},
    "compression": {"package": "vite-plugin-compression", "import": "import compression from 'vite-plugin-compression'", "usage": "compression({ algorithm: 'gzip' })"},
    "svgr": {"package": "vite-plugin-svgr", "import": "import svgr from 'vite-plugin-svgr'", "usage": "svgr()"},
    "eslint": {"package": "vite-plugin-eslint", "import": "import eslint from 'vite-plugin-eslint'", "usage": "eslint()"},
    "md": {"package": "vite-plugin-md", "import": "import Markdown from 'vite-plugin-md'", "usage": "Markdown()"},
    "pwa": {"package": "vite-plugin-pwa", "import": "import { VitePWA } from 'vite-plugin-pwa'", "usage": "VitePWA()"},
    "auto-import": {"package": "unplugin-auto-import", "import": "import AutoImport from 'unplugin-auto-import'", "usage": "AutoImport({ imports: ['react'] })"},
    "components": {"package": "unplugin-vue-components", "import": "import Components from 'unplugin-vue-components'", "usage": "Components()"},
}


def generate_config(detect_result, user_options):
    framework = user_options.get("framework") or detect_result.get("framework", ["react"])
    extra_plugins = user_options.get("extra_plugins", [])

    plugin_imports = []
    plugin_usages = []
    install_deps = []

    for fw in framework:
        if fw in PLUGIN_DEPS:
            d = PLUGIN_DEPS[fw]
            plugin_imports.append(d["import"])
            plugin_usages.append("      " + d["usage"] + ",")
            install_deps.append(d["package"])

    for ep in extra_plugins:
        if ep in PLUGIN_DEPS:
            d = PLUGIN_DEPS[ep]
            plugin_imports.append(d["import"])
            plugin_usages.append("      " + d["usage"] + ",")
            install_deps.append(d["package"])

    lines = []
    lines.append("/**")
    lines.append(" * ViteForge auto-generated vite.config.ts")
    fw_str = ", ".join(framework)
    lines.append(" * Framework: " + fw_str)
    lines.append(" * Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    lines.append(" */")
    lines.append("")
    lines.append("import { defineConfig, loadEnv } from 'vite'")
    lines.append("import { resolve } from 'path'")

    for imp in plugin_imports:
        lines.append(imp)

    lines.append("")
    lines.append("export default defineConfig(({ mode }) => {")
    lines.append("  const env = loadEnv(mode, process.cwd(), '')")
    lines.append("")
    lines.append("  return {")

    # Plugins
    if plugin_usages:
        lines.append("    // ===== Plugins =====")
        lines.append("    plugins: [")
        lines.extend(plugin_usages)
        lines.append("    ],")
        lines.append("")

    # Aliases
    alias_config = user_options.get("alias") or detect_result.get("structure", {}).get("suggested_alias", {})
    if alias_config:
        lines.append("    // ===== Path Aliases =====")
        lines.append("    resolve: {")
        lines.append("      alias: {")
        for k, v in alias_config.items():
            lines.append("        '" + k + "': resolve(__dirname, '" + v + "'),")
        lines.append("      },")
        lines.append("    },")
        lines.append("")

    # Dev server
    lines.append("    // ===== Dev Server =====")
    lines.append("    server: {")
    port = user_options.get("port", 3000)
    lines.append("      port: " + str(port) + ",")
    lines.append("      open: true,")
    proxy = user_options.get("proxy")
    if proxy:
        lines.append("      proxy: {")
        for path, target in proxy.items():
            lines.append("        '" + path + "': '" + target + "',")
        lines.append("      },")
    lines.append("    },")
    lines.append("")

    # Build
    lib_mode = user_options.get("lib_mode")
    if lib_mode:
        lines.append("    // ===== Build (Library Mode) =====")
        lines.append("    build: {")
        lines.append("      lib: {")
        entry = lib_mode.get("entry", "src/index.ts")
        name = lib_mode.get("name", detect_result.get("package_name", "MyLib"))
        lines.append("        entry: resolve(__dirname, '" + entry + "'),")
        lines.append("        name: '" + name + "',")
        lines.append("        formats: ['es', 'umd'],")
        lines.append("        fileName: (format) => `index.${format}.js`,")
        lines.append("      },")
        lines.append("      rollupOptions: {")
        lines.append("        external: ['react', 'react-dom'],")
        lines.append("        output: { globals: { react: 'React' } },")
        lines.append("      },")
        lines.append("    },")
    else:
        lines.append("    // ===== Build =====")
        lines.append("    build: {")
        lines.append("      outDir: 'dist',")
        lines.append("      sourcemap: mode === 'development',")
        lines.append("      chunkSizeWarningLimit: 1000,")
        lines.append("    },")

    lines.append("")
    lines.append("  }")
    lines.append("})")

    return {
        "config": "\n".join(lines),
        "install_deps": list(set(install_deps)),
    }


def main():
    parser = argparse.ArgumentParser(description="ViteForge config generator")
    parser.add_argument("--root", default=os.getcwd(), help="Project root directory")
    parser.add_argument("--framework", help="Framework (react/vue/svelte)")
    parser.add_argument("--proxy", help="Proxy config as JSON")
    parser.add_argument("--alias", help="Alias config as JSON")
    parser.add_argument("--port", type=int, default=3000)
    parser.add_argument("--extra-plugins", help="Extra plugins, comma-separated")
    parser.add_argument("--lib", help="Library mode config as JSON")
    parser.add_argument("--detect-file", help="JSON file from project_detect.py")
    args = parser.parse_args()

    detect_result = {}
    if args.detect_file and os.path.exists(args.detect_file):
        with open(args.detect_file, encoding="utf-8") as f:
            detect_result = json.load(f)

    framework = [args.framework] if args.framework else detect_result.get("framework", ["react"])
    alias = json.loads(args.alias) if args.alias else {}
    proxy = json.loads(args.proxy) if args.proxy else {}
    lib_mode = json.loads(args.lib) if args.lib else None
    extra = [p.strip() for p in args.extra_plugins.split(",")] if args.extra_plugins else []

    result = generate_config(detect_result, {
        "framework": framework,
        "alias": alias,
        "proxy": proxy,
        "port": args.port,
        "extra_plugins": extra,
        "lib_mode": lib_mode,
    })

    print(result["config"])
    if result["install_deps"]:
        print()
        print("// === Required dependencies ===")
        for dep in result["install_deps"]:
            print("// npm i -D " + dep)


if __name__ == "__main__":
    main()
