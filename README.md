# ViteForge ⚒️

> Vite 配置自动生成 — 一句话需求，一把生成完整 vite.config.ts

[![Trae Skill](https://img.shields.io/badge/Trae-Skill-blue)](https://trae.com.cn)
[![Version](https://img.shields.io/badge/version-1.0.0-green)]()

## 这是什么？

ViteForge 是一个 Trae Skill，根据你的项目自动生成 Vite 配置文件。

「React + TypeScript + 代理 /api 到 localhost:3000 + 别名 @/」→ 10 秒出完整 `vite.config.ts`，开箱即用。

## 核心能力

- ✅ 自动检测项目框架（React / Vue / Svelte）
- ✅ 智能识别 TypeScript
- ✅ 配置别名（@/、@lib/）自动生成
- ✅ 代理配置（/api → 后端地址）
- ✅ 环境变量文件识别并自动配 define
- ✅ 常用插件按需装配（visualizer/compression/svg/icons）
- ✅ 库模式 / 多入口 / Electron 等高级场景
- ✅ 生成的配置带中文注释

## 快速开始

### 安装

Trae 设置 → 规则和技能 → 技能 → 创建 → 粘贴 SKILL.md

### 使用

```
生成 Vite 配置：React + TypeScript，代理 /api 到 localhost:8080
```

ViteForge 自动检测项目 → 生成 `vite.config.ts` → 提示需要安装的依赖。

## 支持的技术栈

| 框架 | 语言 | 高级场景 |
|------|------|---------|
| React | TypeScript | 库模式 |
| Vue 3 | JavaScript | MPA 多页面 |
| Svelte | | SSR |
| Vanilla | | Electron |

## 定价

| | 免费版 | Pro 版 |
|------|------|------|
| React/Vue 基础 | ✅ | ✅ |
| 插件列表 | ✅ | ✅ |
| Svelte/Solid | ❌ | ✅ |
| 库模式/SSR/Electron | ❌ | ✅ |
| 增量修改配置 | ❌ | ✅ |
| 价格 | 免费 | 29.9 元 |
