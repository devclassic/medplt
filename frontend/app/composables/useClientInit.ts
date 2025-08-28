import { useWindowSize } from '@vueuse/core'

export const useClientInit = () => {
  const { width } = useWindowSize()

  const scale = computed(() => {
    return width.value / 1920
  })

  watchEffect(() => {
    if (import.meta.client) {
      const el = document.querySelector('.box') as HTMLElement | null
      if (el) {
        el.style.zoom = `${scale.value}`
      }
    }
  })
}
