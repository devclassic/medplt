export default defineNuxtConfig({
  compatibilityDate: '2025-08-28',
  devtools: { enabled: false },
  ssr: false,
  modules: ['@vueuse/nuxt', '@element-plus/nuxt'],
  css: ['element-plus/dist/index.css'],
  elementPlus: {
    importStyle: 'css',
    defaultLocale: 'zh-cn',
  },
  runtimeConfig: {
    public: {
      BASE_URL: import.meta.env.BASE_URL,
    },
  },
  vite: {
    server: {
      allowedHosts: true,
    },
  },
})
