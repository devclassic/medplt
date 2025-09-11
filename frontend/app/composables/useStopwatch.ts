export const useStopwatch = () => {
  const elapsed = ref(0)
  const running = ref(false)
  let lastStart = 0
  // setInterval id
  let timer: any = null

  /* 私有：更新函数，每 1/100 秒触发一次 */
  const update = () => {
    elapsed.value = Date.now() - lastStart
  }

  const start = () => {
    if (running.value) return
    lastStart = Date.now() - elapsed.value
    running.value = true
    timer = setInterval(update, 10)
  }

  const pause = () => {
    if (!running.value) return
    clearInterval(timer)
    running.value = false
  }

  const reset = () => {
    clearInterval(timer)
    elapsed.value = 0
    running.value = false
  }
  
  return { timer, elapsed, running, start, pause, reset }
}

const formatTime = (ms: number) => {
  const pad = (n: number, len = 2) => String(n).padStart(len, '0')
  const h = pad(Math.floor(ms / 3600000))
  const m = pad(Math.floor((ms % 3600000) / 60000))
  const s = pad(Math.floor((ms % 60000) / 1000))
  const cent = pad(Math.floor((ms % 1000) / 10)) // 百分之一秒
  return { h, m, s, cent, str: `${h}:${m}:${s}.${cent}` }
}

const stopwatch = useStopwatch()
const display = computed(() => formatTime(stopwatch.elapsed.value))
const toggle = () => (stopwatch.running.value ? stopwatch.pause() : stopwatch.start())
const reset = () => stopwatch.reset()
