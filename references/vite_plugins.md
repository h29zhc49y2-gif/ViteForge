# Vite 常用插件速查表

## 框架插件

| 场景 | 插件 | 安装 |
|------|------|------|
| React JSX/TSX | @vitejs/plugin-react | `npm i -D @vitejs/plugin-react` |
| React SWC | @vitejs/plugin-react-swc | `npm i -D @vitejs/plugin-react-swc` |
| Vue 3 SFC | @vitejs/plugin-vue | `npm i -D @vitejs/plugin-vue` |
| Vue 3 JSX | @vitejs/plugin-vue-jsx | `npm i -D @vitejs/plugin-vue-jsx` |
| Svelte | @sveltejs/vite-plugin-svelte | `npm i -D @sveltejs/vite-plugin-svelte` |
| SolidJS | vite-plugin-solid | `npm i -D vite-plugin-solid` |

## CSS / 样式

| 场景 | 插件 | 安装 |
|------|------|------|
| Windi CSS | vite-plugin-windicss | `npm i -D vite-plugin-windicss windicss` |
| UnoCSS | unocss | `npm i -D unocss @unocss/preset-uno` |
| Tailwind CSS | (PostCSS 内置) | `npm i -D tailwindcss postcss autoprefixer` |
| Sass/SCSS | (内置) | `npm i -D sass` |
| Less | (内置) | `npm i -D less` |

## 资源处理

| 场景 | 插件 | 安装 |
|------|------|------|
| SVG 组件化 | vite-plugin-svgr | `npm i -D vite-plugin-svgr` |
| SVG Sprite | vite-plugin-svg-icons | `npm i -D vite-plugin-svg-icons` |
| Markdown 导入 | vite-plugin-md | `npm i -D vite-plugin-md` |
| 图片压缩 | vite-plugin-imagemin | `npm i -D vite-plugin-imagemin` |
| WebP 转换 | vite-plugin-webp | `npm i -D vite-plugin-webp` |

## 构建优化

| 场景 | 插件 | 安装 |
|------|------|------|
| 打包分析 | rollup-plugin-visualizer | `npm i -D rollup-plugin-visualizer` |
| Gzip 压缩 | vite-plugin-compression | `npm i -D vite-plugin-compression` |
| Brotli 压缩 | vite-plugin-compression2 | `npm i -D vite-plugin-compression2` |
| 传统浏览器 | @vitejs/plugin-legacy | `npm i -D @vitejs/plugin-legacy terser` |
| 包大小检查 | vite-plugin-checker | `npm i -D vite-plugin-checker` |

## 开发体验

| 场景 | 插件 | 安装 |
|------|------|------|
| 自动导入 API | unplugin-auto-import | `npm i -D unplugin-auto-import` |
| 组件自动注册 | unplugin-vue-components | `npm i -D unplugin-vue-components` |
| ESLint 检查 | vite-plugin-eslint | `npm i -D vite-plugin-eslint eslint` |
| Stylelint | vite-plugin-stylelint | `npm i -D vite-plugin-stylelint stylelint` |
| 类型检查 | vite-plugin-checker | `npm i -D vite-plugin-checker vue-tsc` |
| PWA | vite-plugin-pwa | `npm i -D vite-plugin-pwa` |
| 静态资源复制 | vite-plugin-static-copy | `npm i -D vite-plugin-static-copy` |

## 高级场景

| 场景 | 插件 | 安装 |
|------|------|------|
| Electron | vite-plugin-electron | `npm i -D vite-plugin-electron electron` |
| Electron Renderer | vite-plugin-electron-renderer | `npm i -D vite-plugin-electron-renderer` |
| SSR | (Vite 内置) | 无需额外插件 |
| SSG | vite-ssg | `npm i -D vite-ssg` |
| Web Extension | vite-plugin-web-extension | `npm i -D vite-plugin-web-extension` |
| Condition 编译 | vite-plugin-conditional-compiler | `npm i -D vite-plugin-conditional-compiler` |
| HTML 模板 | vite-plugin-html | `npm i -D vite-plugin-html` |

## 常用插件组合推荐

### React 项目

```bash
npm i -D @vitejs/plugin-react
# 可选增强
npm i -D rollup-plugin-visualizer vite-plugin-compression vite-plugin-svgr
```

### Vue 3 项目

```bash
npm i -D @vitejs/plugin-vue
# 可选增强
npm i -D unplugin-auto-import unplugin-vue-components rollup-plugin-visualizer
```

### 组件库项目

```bash
npm i -D @vitejs/plugin-react vite-plugin-dts
# vite-plugin-dts: 自动生成 .d.ts 类型声明
```
