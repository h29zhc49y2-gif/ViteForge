# ViteForge 项目简报

## 项目概要

- **项目名**：ViteForge
- **定位**：Vite 配置自动生成 Trae Skill，一句需求 → 完整 vite.config.ts
- **一句话**：告诉它 "React + TS + 代理/api到后端 + 别名@"，10 秒生成可直接用的完整 Vite 配置
- **工作区路径**：C:\AI_Projects\ViteForge
- **目标用户**：用 Trae 做前端开发的开发者（React/Vue/Svelte/Library）

## 核心功能

1. 自动检测项目技术栈（框架/语言/包管理器）
2. 按需生成完整 vite.config.ts（plugins/alias/proxy/env/build）
3. 依赖自动安装提示（缺哪个插件装哪个）
4. Webpack → Vite 迁移辅助
5. 多环境配置（dev/preview/prod）
6. 常见场景模板库（SPA/MPA/组件库/Electron）

## 差异化

- 不是 "给一个通用模板"，而是根据项目实际文件结构生成
- 内置 30+ 插件配置模板，知道 peerDependencies
- 代理、别名、环境变量全自动推断
- 生成的配置有中文注释解释每行的作用

## 定价

- 免费版：React/Vue 基础模板 + 插件列表
- Pro 版：29.9元，多框架 + 高级场景(库模式/SSR/Electron) + 增量修改

## 技术架构

```
ViteForge/
├── SKILL.md
├── README.md
├── PROJECT_BRIEF.md
├── scripts/
│   ├── generate_vite_config.py   → 核心生成脚本
│   └── project_detect.py         → 项目检测
├── assets/
│   └── vite_templates.json       → 20+ 场景模板库
├── references/
│   ├── vite_plugins.md           → 插件速查表
│   └── build_tools_map.md        → Webpack→Vite 映射
└── examples/                     → react-ts / vue-ts / library
```

## 与 i18nFlow 关系

同属 "开发者效率工具 Skill 矩阵" 第二个产品，共用分发策略（掘金+飞书+GitHub）。
