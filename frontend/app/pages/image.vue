<template>
  <div class="wrap">
    <div class="title">辅助影像</div>
    <div class="top-box">
      <div ref="result" class="result">
        <div v-for="item in state.messages" :class="{ right: item.pos === 'right' }" class="item">
          <div v-html="item.content" class="content"></div>
        </div>
      </div>
    </div>
    <div class="bottom-box">
      <div class="input-box">
        <div class="toolbar">
          <div class="left">
            <input
              @change="imgFileChange"
              ref="imgfile"
              type="file"
              accept="image/*"
              multiple
              class="file" />
            <input @change="dcmFileChange" ref="dcmfile" type="file" multiple class="file" />
            <div @click="state.imgFileRef.click()" class="upimage"></div>
            <div @click="state.dcmFileRef.click()" class="updicom"></div>
          </div>
          <div class="right">
            <div class="status">{{ state.status }}</div>
            <div @click="asr" class="speech"></div>
            <div @click="clean" class="clean"></div>
          </div>
        </div>
        <textarea
          v-model="state.prompt"
          @keydown.prevent.enter="submit"
          placeholder="请上传片子并输入相关问题"
          class="input"></textarea>
        <div class="bottom">
          <div @click="submit" class="submit"></div>
        </div>
      </div>
      <div class="image-box">
        <div class="images">
          <img v-for="item of state.images" @click="preview(item)" :src="item" class="img" />
        </div>
      </div>
    </div>
  </div>

  <el-dialog v-model="state.showPreview" title="图像预览" width="800">
    <img :src="state.previewUrl" class="preview" />
  </el-dialog>
</template>

<script setup>
  import { fetchEventSource } from '@microsoft/fetch-event-source'
  import markdownit from 'markdown-it'
  const http = useAxios()

  const state = reactive({
    messages: [],
    prompt: '',
    showPreview: false,
    previewUrl: '',
    images: [],
    imgs: [],
    status: '',
    history: [
      {
        role: 'system',
        content: [{ type: 'text', text: '你是端点科技专业医疗影像助手' }],
      },
    ],
    imgFileRef: useTemplateRef('imgfile'),
    dcmFileRef: useTemplateRef('dcmfile'),
    resultRef: useTemplateRef('result'),
  })

  const imgFileChange = e => {
    state.images = []
    const files = e.target.files
    for (let i = 0; i < files.length; i++) {
      const file = files[i]
      state.images.push(URL.createObjectURL(file))
    }
  }

  const dcmFileChange = async e => {
    state.imgFileRef.value = null
    state.status = '上传DCM影像中...'
    state.images = []
    const formData = new FormData()
    const files = e.target.files
    for (let i = 0; i < files.length; i++) {
      const file = files[i]
      formData.append('files', file)
    }
    const res = await http.post('/api/client/image/updcm', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    if (res.data.success) {
      state.images = res.data.data.images.map(item => config.public.BASE_URL + item)
      state.imgs = res.data.data.imgs
    } else {
      ElMessage.error(res.data.message)
    }
    state.status = ''
  }

  let recording = false
  const recorder = useRecorder()
  const asr = async () => {
    if (!recording) {
      state.status = recorder.start(
        () => {
          state.status = '录音中...'
          recording = true
        },
        () => {
          state.status = '录音失败...'
          recording = false
        }
      )
    } else {
      state.status = '正在识别...'
      const res = await recorder.getResult()
      state.prompt = res.data[0].text
      state.status = ''
      recording = false
    }
  }

  const preview = url => {
    state.previewUrl = url
    state.showPreview = true
  }

  const clean = () => {
    state.messages = []
    state.images = []
    state.imgs = []
    state.status = ''
    state.prompt = ''
    state.history = [
      {
        role: 'system',
        content: [{ type: 'text', text: '你是端点科技专业医疗影像助手' }],
      },
    ]
  }

  const md = markdownit()
  const config = useRuntimeConfig()
  const submit = async () => {
    if (state.images.length === 0) {
      ElMessage.error('请上传影像')
      return
    }
    if (!state.prompt) {
      ElMessage.error('请输入提示词')
      return
    }
    state.messages.push({
      pos: 'right',
      content: state.prompt,
    })
    await nextTick()
    state.resultRef.scrollTo({
      top: state.resultRef.scrollHeight,
      behavior: 'smooth',
    })
    const msg = reactive({
      content: '',
    })
    state.messages.push(msg)
    state.status = '上传影像中...'
    const files = state.imgFileRef.files
    if (files.length > 0) {
      const formData = new FormData()
      for (let i = 0; i < files.length; i++) {
        const file = files[i]
        formData.append('files', file)
      }
      const res = await http.post('/api/client/image/upimg', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      state.status = '影像上传完成...'
      state.imgs = res.data.data
    }
    state.status = '正在处理...'
    const url = config.public.BASE_URL + '/api/client/image'
    const ctrl = new AbortController()
    let result = ''
    await fetchEventSource(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: state.prompt, history: state.history, imgs: state.imgs }),
      signal: ctrl.signal,
      async onopen(e) {
        if (e.ok && e.headers.get('content-type')?.includes('text/event-stream')) {
          state.prompt = ''
          console.log('✅ SSE opened')
        } else {
          throw new Error(await e.text())
        }
      },
      async onmessage(e) {
        try {
          const chunk = JSON.parse(e.data)
          result += chunk.token || ''
          msg.content = md.render(result.replace(/<think>[\s\S]*?<\/think>/g, ''))
          if (chunk.event === 'message_end') {
            state.status = ''
          }
          await nextTick()
          state.resultRef.scrollTo({
            top: state.resultRef.scrollHeight,
            behavior: 'smooth',
          })
        } catch (e) {}
      },
      onerror(err) {
        console.error(err)
        ctrl.abort()
      },
      onclose() {
        state.status = ''
        console.log('🔚 SSE closed')
      },
    })
  }
</script>

<style>
  hr {
    margin: 10px 0;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
  }

  table,
  th,
  td {
    border: 1px solid #ccc;
  }

  th {
    background-color: #f2f2f2;
    padding: 10px;
    text-align: left;
  }

  td {
    padding: 10px;
    text-align: left;
  }
</style>

<style scoped>
  .wrap {
    position: relative;
    height: 100%;
  }

  .title {
    line-height: 1;
    font-size: 22px;
    color: #011f3c;
    padding: 30px 30px 25px 30px;
  }

  .top-box {
    border: 1px solid #e5e6eb;
    border-radius: 20px;
    position: absolute;
    top: 77px;
    left: 30px;
    right: 30px;
    bottom: 350px;
  }

  .result {
    position: absolute;
    top: 20px;
    left: 20px;
    right: 20px;
    bottom: 20px;
    overflow: auto;
  }

  .result .item {
    margin-bottom: 10px;
    display: flex;
  }

  .result .item.right {
    justify-content: end;
  }

  .result .item.right .content {
    background: #f5f5f5;
    padding: 15px 20px;
    border-radius: 10px;
  }

  .bottom-box {
    height: 300px;
    border-radius: 20px;
    position: absolute;
    left: 30px;
    right: 30px;
    bottom: 30px;
    display: flex;
    justify-content: space-between;
  }

  .input-box,
  .image-box {
    width: 49.5%;
    height: 100%;
    border: 1px solid #e5e6eb;
    border-radius: 10px;
    padding: 10px;
  }

  .image-box {
    padding: 25px;
    overflow: auto;
  }

  .images {
    width: fit-content;
    display: flex;
  }

  .img {
    width: 230px;
    height: 230px;
    border-radius: 10px;
    margin-right: 20px;
    cursor: pointer;
    display: block;
  }

  .img:last-child {
    margin-right: 0;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .toolbar .left {
    display: flex;
    align-items: center;
  }

  .toolbar .right {
    display: flex;
    align-items: center;
  }

  .file {
    width: 0;
    height: 0;
    opacity: 0;
  }

  .upimage {
    width: 100px;
    height: 36px;
    background: url('@/assets/images/image-upimg.png') no-repeat center center / 100% 100%;
    cursor: pointer;
  }

  .updicom {
    width: 120px;
    height: 36px;
    background: url('@/assets/images/image-updicom.png') no-repeat center center / 100% 100%;
    cursor: pointer;
    margin-left: 10px;
  }

  .status {
    color: #cccccc;
  }

  .speech {
    width: 16px;
    height: 16px;
    background: url('@/assets/images/icon-speech.png') no-repeat center center / 100% 100%;
    cursor: pointer;
    margin-left: 10px;
  }

  .clean {
    width: 16px;
    height: 16px;
    background: url('@/assets/images/icon-clean.png') no-repeat center center / 100% 100%;
    cursor: pointer;
    margin: 0 10px 0;
  }

  .input {
    width: 100%;
    height: 190px;
    margin: 10px 0 5px 0;
    border: none;
    outline: none;
    border-top: 1px solid #e5e6eb;
    padding: 10px;
    font-size: 14px;
    resize: none;
  }

  .bottom {
    display: flex;
    justify-content: end;
  }

  .submit {
    width: 32px;
    height: 32px;
    background: url('@/assets/images/submit.png') no-repeat center center / 100% 100%;
    cursor: pointer;
  }

  .submit:hover {
    background-image: url('@/assets/images/submit-active.png');
  }

  .preview {
    width: 100%;
  }
</style>
