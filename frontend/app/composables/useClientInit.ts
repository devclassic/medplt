export const useClientInit = () => {
  onMounted(() => {
    const { width } = useWindowSize()

    const scale = computed(() => {
      return width.value / 1920
    })

    watchEffect(() => {
      const el = document.querySelector('.box') as HTMLElement | null
      if (el) {
        el.style.zoom = `${scale.value}`
      }
    })
  })
}
