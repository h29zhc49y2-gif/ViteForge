# 新项目配 Vite 配置又花了我 30 分钟，于是我写了个 Trae Skill，10 秒搞定

> 一个自动检测项目、按需生成 Vite 配置的 Trae Skill，开源免费，装上就用。

---

## 你是不是也经历过这种抓狂？

新项目初始化，你打算从 Webpack 切到 Vite。打开官方文档，开始：

- 翻看插件列表，"React 需要 `@vitejs/plugin-react`，Vue 需要 `@vitejs/plugin-vue`…"
- 配置别名 `@/ → ./src`，手写 `path.resolve(__dirname, './src')`
- 配置代理 `/api → localhost:8080`，还得处理 `changeOrigin` 和路径重写
- 想加个打包分析，搜 "vite bundle analyzer"，发现插件名是 `rollup-plugin-visualizer`
- 配置环境变量 `define`，折腾 `loadEnv` 的 `mode` 参数
- 刚配完，同事说 "我们用 pnpm"，插件安装命令全得改…

**30 分钟后，你终于有了一个能用的 `vite.config.ts`。但里面有一半配置你自己也不确定写得对不对。**

更别提库模式、Electron、MPA 多页面这些高阶场景了——每次都得重新查文档。

**我受够了，于是在 Trae 上做了 ViteForge——一个自动生成 Vite 配置的 Skill。**

---

## ViteForge：一句话生成完整 vite.config.ts

你只需要在 Trae 里说一句话：

```
生成 Vite 配置：React + TypeScript，代理 /api 到 localhost:8080
```

然后 ViteForge 自动：

| 步骤 | 做了什么 | 你手工做要多久 |
|------|----------|--------------|
| 🔍 检测项目 | 自动判断 React/Vue/Svelte/TS/包管理器 | — |
| 🧩 装配插件 | 按框架类型装配必装插件，按需推荐可选插件 | 查文档 5-10 分钟 |
| 🔗 配置别名 | 自动推断 `@/ → src/` 等路径别名 | 手写配置 2 分钟 |
| 🔄 配置代理 | 处理单代理/多代理/WebSocket/路径重写 | 查文档+调试 5 分钟 |
| 🌐 环境变量 | 自动识别 `.env*` 文件，配置 `define` 暴露 | 读文档 3 分钟 |
| 📦 安装提示 | 给出 pnpm/npm/yarn 安装命令 | 逐条拼命令 |
| 📝 中文注释 | 每行关键配置附中文解释 | 自己写注释 |

整个过程 10 秒钟，输出一个带中文注释、可直接使用的完整配置文件。

---

## 效果对比

### 手工配置（真实经历）

```
项目框架：React + TypeScript
需求：别名 @/、代理 /api、打包分析、Gzip 压缩
─────────────────────────────
查 Vite 文档熟悉配置结构：10 分钟
找插件并确认包名：5 分钟
手写 alias + proxy：5 分钟
配置 visualizer + compression：5 分钟
处理 TypeScript 路径类型：3 分钟
调试、修错：5 分钟
总计：约 30 分钟
```

### ViteForge（同一项目实测）

```
项目框架：React + TypeScript
需求：别名 @/、代理 /api、打包分析、Gzip 压缩
─────────────────────────────
一句话输入：10 秒
检查输出是否合理：20 秒
npm install 依赖：30 秒
总计：1 分钟
```

**效率提升 30 倍**。生成的配置比手工写得还规范——因为内置了 30+ 插件的最佳实践配置模板。

---

## 比用 ChatGPT 直接问强在哪？

你可能会想：我不直接问 ChatGPT 写 Vite 配置？

可以，但有这些坑：

| 场景 | ChatGPT 直接生成 | ViteForge |
|------|---------------|-----------|
| 项目感知 | ❌ 不知道你项目有没有 TS、用的什么包管理器 | ✅ 自动检测 package.json、tsconfig.json |
| 插件版本 | ❌ 可能给出过时的插件名或 API | ✅ 内置 30+ 插件最新配置模板 |
| 别名推断 | ❌ 需要你手动告诉它目录结构 | ✅ 自动扫描 src/components/lib 等目录 |
| 安装命令 | ❌ 默认给 npm，不会根据项目适配 | ✅ 自动识别 npm/pnpm/yarn/bun |
| 中文注释 | ❌ 生成英文注释或没注释 | ✅ 每条关键配置带中文解释 |
| 特殊场景 | ❌ 库模式/Electron/MPA 容易配错 | ✅ 内置 4 种高级场景模板 |

简单说：ChatGPT 给你一个"看起来对"的配置，ViteForge 给你一个"检查过你的项目，确认能跑"的配置。

---

## 3 步安装，30 秒搞定

### 方式一：飞书文档（推荐，国内秒开）

打开文档 → 全选代码块 → 复制 → 粘贴到 Trae：

👉 **[ViteForge 安装文档](https://ycnxanoj4gnj.feishu.cn/wiki/Polywa2G3iY6WtkQ7lIcIOkfn6J)**（待替换为实际飞书链接）

### 方式二：GitHub / Gitee

直接下载 SKILL.md：

👉 [GitHub - ViteForge](https://github.com/h29zhc49y2-gif/ViteForge) ｜ [Gitee 镜像（国内秒开）](https://gitee.com/neshama_ai/ViteForge)

### 粘贴位置

打开 Trae → 设置 → 规则和技能 → 技能 → 创建 → 粘贴 → 保存

---

## 使用示例

### 场景 1：新项目从零搭建

```
生成 Vite 配置：Vue3 + TypeScript，代理 /api 到 localhost:3000
```

ViteForge 自动检测项目 → 装配 `@vitejs/plugin-vue` → 配置别名 `@/` 和代理 → 输出 `vite.config.ts` → 提示 `npm i -D @vitejs/plugin-vue`。

### 场景 2：从 Webpack 迁移

```
把 Webpack 配置迁移到 Vite，项目是 React + TS，有别名 @/ 指向 src/
```

ViteForge 映射 Webpack 配置 → 生成等效 Vite 配置 → 列出哪些 loader 用哪个插件替代。

### 场景 3：高阶场景

```
生成 Vite 库模式配置：入口 src/index.ts，输出 es + umd，不打包 react
```

ViteForge 自动生成 `build.lib` 配置，正确设置 `external` 和 `globals`。

### 场景 4：增量修改

```
给我的 Vite 配置加 Gzip 压缩和打包分析
```

ViteForge 读取现有配置 → 追加插件 → 给出安装命令，不动已有配置。

---

## 支持的技术栈

| 框架 | 语言 | 高级场景 |
|------|------|---------|
| React | TypeScript | 库模式 (Library Mode) |
| Vue 3 | JavaScript | MPA 多页面 |
| Svelte | | SSR 服务端渲染 |
| Vanilla | | Electron 桌面应用 |

### 内置 30+ 插件配置模板

React / Vue / Svelte / visualizer / compression / svgr / eslint / Markdown / PWA / auto-import / components / WindiCSS / Unocss ……

---

## 免费使用，欢迎反馈

ViteForge 完全开源免费。和 [i18nFlow](https://juejin.cn/post/7650883011774595123) 一样，是我"开发者效率工具"矩阵的第二款产品。

如果你用了觉得好用，欢迎在评论区告诉我；如果遇到 bug 或者想支持新插件，也欢迎提 Issue。

👇 安装走起：

> 🔗 **[ViteForge 安装文档（飞书，秒开）]()** （待发布飞书链接后更新）
> 
> 💻 [GitHub](https://github.com/h29zhc49y2-gif/ViteForge) ｜ [Gitee（国内秒开）](https://gitee.com/neshama_ai/ViteForge)

---

*#Trae #Vite #前端工程化 #效率工具 #AI编程 #构建工具*
