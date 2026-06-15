---
name: ViteForge
description: >
  鏍规嵁椤圭洰鑷姩鐢熸垚 Vite 閰嶇疆鏂囦欢銆傝嚜鍔ㄦ娴?React/Vue/Svelte 妗嗘灦銆?  閰嶇疆鍒悕鍜屼唬鐞嗐€佽閰嶅父鐢ㄦ彃浠躲€傛敮鎸佸簱妯″紡/MPA/SSR/Electron 绛夊満鏅€?  鐢熸垚鐨勯厤缃甫涓枃娉ㄩ噴锛屽紑绠卞嵆鐢ㄣ€?version: 1.0.0
tags: [Vite, 閰嶇疆, 鏋勫缓宸ュ叿, 宸ョ▼鍖? 鍓嶇, bundler]
triggers:
  - 鐢熸垚Vite閰嶇疆
  - 鍒涘缓vite.config
  - Vite閰嶇疆
  - 鍒濆鍖朧ite
  - 閰峍ite
  - vite椤圭洰閰嶇疆
  - vite config
  - 鎼缓vite
  - Vite鎻掍欢閰嶇疆
  - vite build config
---

# ViteForge

## 浠诲姟鐩爣

鏍规嵁椤圭洰瀹為檯鏂囦欢缁撴瀯鍜岀敤鎴烽渶姹傦紝鐢熸垚鍙洿鎺ヤ娇鐢ㄧ殑瀹屾暣 `vite.config.ts`銆?
## 鎵ц娴佺▼

### Step 1锛氭娴嬮」鐩幆澧?
杩愯妫€娴嬭剼鏈細
```bash
python scripts/project_detect.py "<椤圭洰鏍圭洰褰?"
```

鑾峰彇锛氭鏋剁被鍨?鏄惁TS/鍖呯鐞嗗櫒/鐜版湁 Vite 鎻掍欢/package.json 鍐呭

### Step 2锛氱悊瑙ｇ敤鎴烽渶姹?
浠庣敤鎴疯緭鍏ユ彁鍙栵細
- 鎶€鏈爤锛圧eact/Vue/Svelte锛岄粯璁や粠妫€娴嬬粨鏋滄帹鏂級
- 鍒悕閰嶇疆锛堝 @/ 鈫?src/锛岄粯璁よ嚜鍔ㄦ帹鏂級
- 浠ｇ悊鐩爣锛堝 /api 鈫?http://localhost:8080锛?- 鐗规畩鍦烘櫙锛堝簱妯″紡/MPA澶氶〉/SSR/Electron锛?- 棰濆鎻掍欢锛坴isualizer/compression/绛夛級

### Step 3锛氱敓鎴愰厤缃?
璋冪敤鐢熸垚鑴氭湰锛?```bash
python scripts/generate_vite_config.py --root <椤圭洰鏍圭洰褰? [閫夐」...]
```

### Step 4锛氳緭鍑轰笌妫€鏌?
- 杈撳嚭鐢熸垚鐨?`vite.config.ts` 鍐呭锛堝甫娉ㄩ噴锛?- 鍒楀嚭闇€瑕佸畨瑁呯殑渚濊禆锛坣pm/pnpm/yarn 鍛戒护锛?- 琛ュ厖浣跨敤璇存槑锛坣pm run dev / npm run build锛?
---

## 鏍稿績瑙勫垯

### 瑙勫垯 1锛氬埆鍚嶈嚜鍔ㄦ帹鏂?
鏍规嵁椤圭洰缁撴瀯鎺ㄦ柇鍒悕锛屽父瑙佹ā寮忥細

| 鐩綍瀛樺湪 | 鍒悕閰嶇疆 |
|---------|---------|
| src/ | @/ 鈫?./src |
| src/ + components/ | @/ 鈫?./src |
| lib/ | @lib/ 鈫?./lib |
| packages/ | monorepo 澶氬叆鍙?|

鑻?package.json 宸叉湁 paths 閰嶇疆锛屼紭鍏堜娇鐢ㄣ€?
### 瑙勫垯 2锛氫唬鐞嗛厤缃?
绠€鍗曚唬鐞嗭細
```ts
server: {
  proxy: {
    '/api': 'http://localhost:8080'
  }
}
```

澶嶆潅浠ｇ悊锛堝涓悗绔?WebSocket锛夛細
```ts
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8080',
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, '')
    },
    '/ws': {
      target: 'ws://localhost:8080',
      ws: true
    }
  }
}
```

### 瑙勫垯 3锛氭彃浠舵寜闇€瑁呴厤

| 鍦烘櫙 | 鎺ㄨ崘鎻掍欢 | 闇€瑕佸畨瑁?|
|------|---------|---------|
| React | @vitejs/plugin-react | npm i -D @vitejs/plugin-react |
| Vue 3 | @vitejs/plugin-vue | npm i -D @vitejs/plugin-vue |
| Svelte | @sveltejs/vite-plugin-svelte | npm i -D @sveltejs/vite-plugin-svelte |
| TypeScript | (鍐呯疆) | 鏃犻渶棰濆鎻掍欢 |
| 璺緞鍒悕 | (鍐呯疆 resolve.alias) | 鏃犻渶棰濆鎻掍欢 |
| 鎵撳寘鍒嗘瀽 | rollup-plugin-visualizer | npm i -D rollup-plugin-visualizer |
| 鍘嬬缉 | vite-plugin-compression | npm i -D vite-plugin-compression |
| SVG 缁勪欢 | vite-plugin-svgr | npm i -D vite-plugin-svgr |
| 鑷姩瀵煎叆 | unplugin-auto-import | npm i -D unplugin-auto-import |
| 缁勪欢鑷姩娉ㄥ唽 | unplugin-vue-components | npm i -D unplugin-vue-components |
| PWA | vite-plugin-pwa | npm i -D vite-plugin-pwa |
| WindiCSS | vite-plugin-windicss | npm i -D vite-plugin-windicss |
| Unocss | unocss | npm i -D unocss |
| ESLint | vite-plugin-eslint | npm i -D vite-plugin-eslint |
| Markdown | vite-plugin-md | npm i -D vite-plugin-md |
| 鐜鍙橀噺 | (鍐呯疆 loadEnv) | 鏃犻渶棰濆鎻掍欢 |

### 瑙勫垯 4锛氱敓鎴愰厤缃繀椤诲寘鍚殑娉ㄩ噴

姣忚鍏抽敭閰嶇疆閮借娉ㄩ噴浣滅敤锛屽府鍔╁紑鍙戣€呯悊瑙ｏ細
```ts
// ===== 璺緞鍒悕 =====
resolve: {
  alias: {
    '@': path.resolve(__dirname, './src'),  // @/ 鎸囧悜 src 鐩綍
  }
}
```

### 瑙勫垯 5锛氬畬鏁撮厤缃粨鏋?
```ts
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd())  // 鍔犺浇 .env 鏂囦欢
  
  return {
    // ===== 鎻掍欢 =====
    plugins: [react()],
    
    // ===== 璺緞鍒悕 =====
    resolve: {
      alias: { '@': resolve(__dirname, './src') }
    },
    
    // ===== 寮€鍙戞湇鍔″櫒 =====
    server: {
      port: 3000,
      proxy: { '/api': 'http://localhost:8080' }
    },
    
    // ===== 鏋勫缓閰嶇疆 =====
    build: {
      outDir: 'dist',
      sourcemap: mode === 'development',
    }
  }
})
```

---

## 鐗规畩鍦烘櫙

### 搴撴ā寮?```ts
build: {
  lib: {
    entry: resolve(__dirname, 'src/index.ts'),
    name: 'MyLib',
    formats: ['es', 'umd'],
    fileName: (format) => `my-lib.${format}.js`
  },
  rollupOptions: {
    external: ['react', 'react-dom'],  // 涓嶆墦鍖呰繘搴?    output: { globals: { react: 'React' } }
  }
}
```

### MPA 澶氶〉闈?```ts
build: {
  rollupOptions: {
    input: {
      main: resolve(__dirname, 'index.html'),
      admin: resolve(__dirname, 'admin/index.html'),
    }
  }
}
```

### Electron
```ts
// 闇€瑕?vite-plugin-electron
import electron from 'vite-plugin-electron'
plugins: [
  react(),
  electron([{
    entry: 'electron/main.ts',
  }, {
    entry: 'electron/preload.ts',
  }])
]
```

## 鐜鍙橀噺绾﹀畾

鑷姩璇嗗埆 `.env` 鏂囦欢锛?- `.env` 鈥?鎵€鏈夌幆澧?- `.env.development` 鈥?dev
- `.env.production` 鈥?production

```ts
// 浣跨敤 define 鏆撮湶缁欏鎴风
define: {
  __APP_VERSION__: JSON.stringify(env.VITE_APP_VERSION),
}
```

## 鏋勫缓浼樺寲榛樿鍊?
- `build.target: 'es2020'` 鈥?鍏煎鐜颁唬娴忚鍣?- `build.chunkSizeWarningLimit: 1000` 鈥?鎻愰珮鍒嗗潡璀﹀憡闃堝€?- `build.rollupOptions.output.manualChunks` 鈥?鑷姩鎷嗗垎 node_modules