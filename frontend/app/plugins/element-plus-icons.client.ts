import * as ElementPlusIconsVue from '@element-plus/icons-vue'

export default defineNuxtPlugin(nuxtApp => {
  for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    const kebabName = key.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase()
    nuxtApp.vueApp.component(kebabName, component) // 注册 <icon-menu />
    nuxtApp.vueApp.component(key, component) // 注册 <IconMenu />
  }
})
