import Recorder from 'js-audio-recorder'
import { useAxios } from '@/composables/useAxios'

const recorder = new Recorder({
  sampleBits: 16,
  sampleRate: 16000,
  numChannels: 1,
})

export const useRecorder = () => {
  return {
    start(ok = () => {}, err = () => {}) {
      recorder.start().then(
        () => {
          console.log('开始录音')
          ok()
        },
        error => {
          console.log('开始录音失败', error)
          err()
        }
      )
    },
    stop() {
      recorder.stop()
      console.log('停止录音')
    },
    getBlob() {
      this.stop()
      return recorder.getWAVBlob()
    },
    async getResult() {
      const blob = this.getBlob()
      const file = new File([blob], 'audio.wav')
      const formData = new FormData()
      formData.append('file', file)
      const http = useAxios()
      const res = await http.post('/api/client/asr', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      return res.data
    },
  }
}
