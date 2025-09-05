<template>
  <div class="wrap">
    <div class="title">辅助诊疗</div>
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
          <div></div>
          <div class="right">
            <div class="status">{{ state.status }}</div>
            <div @click="asr" class="speech"></div>
            <div @click="clean" class="clean"></div>
          </div>
        </div>
        <textarea
          v-model="state.prompt"
          @keydown.prevent.enter="submit"
          placeholder="请输入提示词"
          class="input"></textarea>
        <div class="bottom">
          <div @click="submit" class="submit"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { fetchEventSource } from '@microsoft/fetch-event-source'
  import markdownit from 'markdown-it'

  const state = reactive({
    status: '',
    prompt: '',
    messages: [],
    resultRef: useTemplateRef('result'),
  })

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

  const clean = () => {
    state.status = ''
    state.prompt = ''
    state.messages = []
  }

  const md = markdownit()
  const config = useRuntimeConfig()
  const submit = async () => {
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

    state.status = '生成中...'
    const url = config.public.BASE_URL + '/api/client/assist'
    const ctrl = new AbortController()
    let result = ''
    await fetchEventSource(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: state.prompt }),
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
          result += chunk.answer || ''
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
  }

  .input-box {
    height: 100%;
    border: 1px solid #e5e6eb;
    border-radius: 10px;
    padding: 10px;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 36px;
  }

  .toolbar .right {
    display: flex;
    align-items: center;
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
</style>
