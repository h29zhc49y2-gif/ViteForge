# Webpack 鈫?Vite 鍔熻兘鏄犲皠

## 鏍稿績姒傚康瀵圭収

| Webpack | Vite | 璇存槑 |
|---------|------|------|
| entry | build.rollupOptions.input | Vite 榛樿 index.html 涓哄叆鍙?|
| output.path | build.outDir | 杈撳嚭鐩綍 |
| output.publicPath | base | 鍏叡璺緞 |
| resolve.alias | resolve.alias | 璺緞鍒悕锛堝啓娉曞嚑涔庝竴鏍凤級 |
| resolve.extensions | resolve.extensions | 鎵╁睍鍚嶇渷鐣?|
| devServer | server | 寮€鍙戞湇鍔″櫒 |
| devServer.proxy | server.proxy | 浠ｇ悊閰嶇疆 |
| plugins | plugins | 鎻掍欢 |
| externals | build.rollupOptions.external | 澶栭儴渚濊禆 |
| optimization.splitChunks | build.rollupOptions.output.manualChunks | 浠ｇ爜鍒嗗壊 |

## 甯哥敤 Loader 鈫?瀵瑰簲鏂规

| Webpack Loader | Vite 鏂规 |
|---------------|----------|
| babel-loader | @vitejs/plugin-react (+ esbuild 鍐呯疆) |
| vue-loader | @vitejs/plugin-vue |
| ts-loader | esbuild 鍐呯疆 |
| css-loader/style-loader | Vite 鍐呯疆 CSS 澶勭悊 |
| sass-loader | 瀹夎 sass 鍗冲彲锛圴ite 鍐呯疆锛?|
| less-loader | 瀹夎 less 鍗冲彲锛圴ite 鍐呯疆锛?|
| file-loader/url-loader | Vite 鍐呯疆 import |
| svg-loader | vite-plugin-svgr |
| worker-loader | new Worker(new URL(...), { type: module }) |

## 甯哥敤 Plugins 鈫?瀵瑰簲鏂规

| Webpack Plugin | Vite 鏂规 |
|---------------|----------|
| HtmlWebpackPlugin | Vite 鍐呯疆锛坕ndex.html 涓哄叆鍙ｏ級 |
| DefinePlugin | define 閰嶇疆 |
| CopyWebpackPlugin | vite-plugin-static-copy |
| MiniCssExtractPlugin | Vite 鍐呯疆 CSS code splitting |
| WebpackBundleAnalyzer | rollup-plugin-visualizer |
| CompressionPlugin | vite-plugin-compression |
| HotModuleReplacementPlugin | Vite 鍐呯疆 HMR |
| EnvironmentPlugin | loadEnv + define |