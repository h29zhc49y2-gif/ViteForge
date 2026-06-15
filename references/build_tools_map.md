# Webpack → Vite 功能映射

## 核心概念对照

| Webpack | Vite | 说明 |
|---------|------|------|
| webpack.config.js | vite.config.ts | 配置文件名不同 |
| entry | (基于 HTML 入口) | Vite 以 index.html 为入口 |
| output | build.outDir | 输出目录配置 |
| module.rules | (插件自动处理) | Vite 通过插件处理文件 |
| resolve.alias | resolve.alias | 别名配置方式一致 |
| resolve.extensions | resolve.extensions | 扩展名解析一致 |
| devServer | server | 开发服务器配置 |
| plugins | plugins | 插件系统（API 不同） |
| optimization.splitChunks | build.rollupOptions.output.manualChunks | 代码分割 |
| DefinePlugin | define | 环境变量注入 |
| CopyWebpackPlugin | vite-plugin-static-copy | 静态资源复制 |

## Loader → Plugin 映射

| Webpack Loader | Vite 方案 | 备注 |
|---------------|----------|------|
| babel-loader | @vitejs/plugin-react | Vite 默认用 esbuild |
| vue-loader | @vitejs/plugin-vue | 官方插件 |
| svelte-loader | @sveltejs/vite-plugin-svelte | 官方插件 |
| css-loader + style-loader | (内置) | Vite 原生支持 CSS |
| sass-loader | (内置) | 安装 sass 即可 |
| less-loader | (内置) | 安装 less 即可 |
| postcss-loader | (内置) | 支持 postcss.config.js |
| file-loader / url-loader | (内置) | Vite 自动处理资源 |
| svg-loader | vite-plugin-svgr | SVG 作为组件导入 |
| markdown-loader | vite-plugin-md | Markdown 导入 |
| html-loader | (内置) | Vite 原生支持 |
| worker-loader | (内置) | 支持 Web Worker |
| ts-loader | (内置) | esbuild 编译，不做类型检查 |
| fork-ts-checker | vite-plugin-checker | 类型检查 |
| eslint-loader | vite-plugin-eslint | ESLint 检查 |

## Webpack Plugin → Vite Plugin 映射

| Webpack Plugin | Vite Plugin | 功能 |
|---------------|------------|------|
| HtmlWebpackPlugin | vite-plugin-html | HTML 模板处理 |
| MiniCssExtractPlugin | (内置) | CSS 提取 |
| TerserPlugin | (内置) | JS 压缩 |
| CssMinimizerPlugin | (内置) | CSS 压缩 |
| CompressionPlugin | vite-plugin-compression | Gzip/Brotli 压缩 |
| CopyWebpackPlugin | vite-plugin-static-copy | 静态文件复制 |
| DefinePlugin | (内置 define) | 环境变量替换 |
| BundleAnalyzerPlugin | rollup-plugin-visualizer | 打包分析 |
| WorkboxPlugin | vite-plugin-pwa | PWA 支持 |
| HotModuleReplacement | (内置 HMR) | 热更新 |
| EnvironmentPlugin | (内置 loadEnv) | 环境变量加载 |
| DotenvPlugin | (内置 loadEnv) | .env 文件加载 |
| ProgressPlugin | (内置) | 构建进度 |
| WebpackBar | vite-plugin-progress | 进度条 |

## 常见迁移场景

### 1. 别名 (alias)

```js
// Webpack
resolve: {
  alias: {
    '@': path.resolve(__dirname, 'src'),
    '@components': path.resolve(__dirname, 'src/components')
  }
}

// Vite (几乎一样)
resolve: {
  alias: {
    '@': path.resolve(__dirname, './src'),
    '@components': path.resolve(__dirname, './src/components')
  }
}
```

### 2. 代理 (proxy)

```js
// Webpack
devServer: {
  proxy: {
    '/api': 'http://localhost:8080'
  }
}

// Vite (几乎一样)
server: {
  proxy: {
    '/api': 'http://localhost:8080'
  }
}
```

### 3. 环境变量

```js
// Webpack - webpack.DefinePlugin
new webpack.DefinePlugin({
  'process.env.API_URL': JSON.stringify('https://api.example.com')
})

// Vite - define 配置
define: {
  __API_URL__: JSON.stringify('https://api.example.com')
}
// 注意：Vite 中环境变量需要 VITE_ 前缀才能在客户端访问
// import.meta.env.VITE_API_URL
```

### 4. 代码分割

```js
// Webpack
optimization: {
  splitChunks: {
    chunks: 'all',
    cacheGroups: {
      vendor: {
        test: /node_modules/,
        name: 'vendor'
      }
    }
  }
}

// Vite (使用 Rollup 的 manualChunks)
build: {
  rollupOptions: {
    output: {
      manualChunks: {
        vendor: ['react', 'react-dom'],
        utils: ['lodash', 'dayjs']
      }
    }
  }
}
```

## 迁移注意事项

1. **CommonJS → ESM**：Vite 要求使用 ES Module 语法 (`import`/`export`)
2. **require.context**：Vite 使用 `import.meta.glob` 替代
3. **process.env**：客户端代码中使用 `import.meta.env` 替代
4. **__dirname**：Vite 中需要通过 `path.resolve()` 获取绝对路径
5. **CSS Modules**：文件名需改为 `*.module.css` 格式
6. **静态资源**：放在 `public/` 目录下，通过绝对路径引用
7. **类型检查**：Vite 默认不做 TS 类型检查，需要单独运行 `tsc --noEmit`
