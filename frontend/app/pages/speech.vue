<template>
  <div class="wrap">
    <div class="title">多人语音</div>
    <div class="top-box">
      <div ref="result" v-html="state.result" class="result"></div>
    </div>
    <div class="bottom-box">
      <div class="input-box">
        <div class="toolbar">
          <div class="left">
            <div @click="state.showType = !state.showType" class="type"></div>
            <div v-show="state.showType" class="type-list">
              <div @click="typeMR(item.content)" v-for="item in state.types" class="item">
                <div class="icon icon-mr"></div>
                <div class="text">{{ item.name }}</div>
              </div>
              <div @click="typeCustom" class="item">
                <div class="icon icon-custom"></div>
                <div class="text">自定义</div>
              </div>
              <div @click="state.showType = false" class="item">
                <div class="icon icon-clean"></div>
                <div class="text">取消</div>
              </div>
            </div>
            <div @click="showCustomize" class="customize"></div>
          </div>
          <div class="right">
            <div class="status">{{ state.status }}</div>
            <div @click="asr" :class="{ active: recording }" class="speech"></div>
            <div @click="clean" class="clean"></div>
          </div>
        </div>
        <textarea
          v-model="state.prompt"
          @keydown.prevent.enter="submit"
          placeholder="请输入对话生成提示词，对话内容为<对话>"
          class="input"></textarea>
        <div class="bottom">
          <div @click="submit" class="submit"></div>
        </div>
      </div>
      <div class="speech-box">
        <div class="toolbar">
          <div class="left">
            <div @click="showRename" class="rename"></div>
            <div @click="save" class="save"></div>
            <input
              type="file"
              ref="upaudio"
              @change="upAudioChnage"
              style="width: 0; height: 0; opacity: 0" />
            <div @click="upload" class="upload"></div>
          </div>
        </div>
        <div class="speech-list">
          <div v-for="item of state.speechItems" class="item">
            <span class="name">{{ item.name }}：</span>
            <span class="content">{{ item.text }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <el-dialog v-model="state.showRename" title="命名说话人" width="500">
    <el-form label-width="auto">
      <el-form-item v-for="(name, i) in state.names" :label="name">
        <el-input v-model="state.nameValues[i]" />
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="state.showRename = false">取消</el-button>
      <el-button type="primary" @click="rename">确定</el-button>
    </template>
  </el-dialog>

  <el-dialog v-model="state.showCustomize" title="自定义生成类型" width="600">
    <el-button @click="showEditType('add')" type="primary" style="margin-bottom: 10px">
      添加类型
    </el-button>
    <el-table :data="state.tableData" stripe border>
      <el-table-column prop="name" label="类型名称" />
      <el-table-column label="操作">
        <template #default="scope">
          <el-button link type="primary" size="small" @click="showEditType('update', scope.row)">
            修改
          </el-button>
          <el-button link type="danger" size="small" @click="deleteType(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <template #footer>
      <el-button @click="state.showCustomize = false">取消</el-button>
      <el-button type="primary" @click="state.showCustomize = false">确定</el-button>
    </template>
  </el-dialog>

  <el-dialog v-model="state.showEditType" title="添加类型" width="600">
    <el-form label-width="auto">
      <el-form-item label="名称">
        <el-input v-model="state.type.name" />
      </el-form-item>
      <el-form-item label="内容">
        <el-input v-model="state.type.content" type="textarea" :rows="8" />
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="state.showEditType = false">取消</el-button>
      <el-button type="primary" @click="editType()">确定</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
  import { fetchEventSource } from '@microsoft/fetch-event-source'
  import markdownit from 'markdown-it'

  const state = reactive({
    showType: false,
    showRename: false,
    status: '',
    prompt: '',
    names: [],
    nameValues: [],
    speechItems: [],
    result: '',
    resultRef: useTemplateRef('result'),
    url: '',
    upaudio: useTemplateRef('upaudio'),
    showCustomize: false,
    tableData: [],
    showEditType: false,
    type: {
      id: '',
      name: '',
      content: '',
    },
    opened: false,
    act: '',
    types: [],
  })

  const http = useAxios()

  const updateTypes = async () => {
    const res = await http.post('/api/client/types')
    state.types = res.data.data
  }

  updateTypes()

  const showCustomize = async () => {
    const res = await http.post('/api/client/types')
    state.tableData = res.data.data
    state.showCustomize = true
  }

  const showEditType = (act, row) => {
    if (act === 'add') {
      state.type.id = ''
      state.type.name = ''
      state.type.content = ''
    } else if (act === 'update') {
      state.type.id = row.id
      state.type.name = row.name
      state.type.content = row.content
    }
    state.showEditType = true
    state.act = act
  }

  const editType = async () => {
    if (state.act === 'add') {
      await http.post('/api/client/types/add', state.type)
    } else if (state.act === 'update') {
      await http.post('/api/client/types/update', state.type)
    }
    state.showEditType = false
    showCustomize()
    updateTypes()
  }

  const deleteType = async row => {
    await http.post('/api/client/types/delete', { id: row.id })
    showCustomize()
    updateTypes()
  }

  const dialog = () => {
    let text = ''
    state.speechItems.forEach(item => {
      text += `${item.name}：${item.text}\n`
    })
    return `<对话>${text}</对话>`
  }

  const typeMR = content => {
    state.prompt = content
    state.showType = false
  }

  const typeCustom = () => {
    state.prompt = ''
    state.showType = false
  }

  const stopwatch = useStopwatch()
  const formatTime = ms => {
    const pad = (n, len = 2) => String(n).padStart(len, '0')
    const h = pad(Math.floor(ms / 3600000))
    const m = pad(Math.floor((ms % 3600000) / 60000))
    const s = pad(Math.floor((ms % 60000) / 1000))
    const cent = pad(Math.floor((ms % 1000) / 10)) // 百分之一秒
    return { h, m, s, cent, str: `${h}:${m}:${s}` }
  }
  const display = computed(() => formatTime(stopwatch.elapsed.value))
  const recorder = useRecorder()

  let recording = ref(false)
  let timer = null
  const asr = async () => {
    if (!recording.value) {
      state.status = '开始收音...'
      recorder.start(
        () => {
          stopwatch.start()
          state.status = `${display.value.str} 录音中...`
          timer = setInterval(() => {
            state.status = `${display.value.str} 录音中...`
          }, 100)
          recording.value = true
        },
        () => {
          clearInterval(timer)
          stopwatch.reset()
          state.status = '录音失败...'
          recording.value = false
        }
      )
    } else {
      state.status = '生成对话...'
      clearInterval(timer)
      stopwatch.reset()
      const res = await recorder.getResult()
      const items = res.data[0]?.sentence_info
      state.url = res.data[0]?.url
      if (items) {
        state.speechItems = items.map(item => ({
          name: `说话人${item.spk}`,
          spk: item.spk,
          text: item.text,
        }))
      }
      state.status = ''
      recording.value = false
    }
  }

  const showRename = () => {
    state.names = [...new Set(state.speechItems.map(item => item.name))]
    state.showRename = true
  }

  const rename = () => {
    state.speechItems.forEach(item => {
      item.name = state.nameValues[state.names.indexOf(item.name)]
    })
    state.showRename = false
  }

  const md = markdownit()
  const config = useRuntimeConfig()
  const submit = async () => {
    if (!state.prompt) {
      ElMessage.error('请输入对话生成提示词')
      return
    }
    state.status = '生成中...'
    const prompt = `${dialog()}\n${state.prompt}`
    const url = config.public.BASE_URL + '/api/client/asr/generate'
    const ctrl = new AbortController()
    let result = ''
    await fetchEventSource(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt }),
      signal: ctrl.signal,
      async onopen(e) {
        if (e.ok && e.headers.get('content-type')?.includes('text/event-stream')) {
          console.log('✅ SSE opened')
        } else {
          throw new Error(await e.text())
        }
      },
      async onmessage(e) {
        try {
          const chunk = JSON.parse(e.data)
          result += chunk.answer || ''
          state.result = md.render(result.replace(/<think>[\s\S]*?<\/think>/g, ''))
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

  const save = () => {
    if (!state.url) {
      ElMessage.error('暂未生成录音')
      return
    }
    const a = document.createElement('a')
    a.target = '_blank'
    a.href = config.public.BASE_URL + state.url
    a.download = '录音.wav'
    a.click()
  }

  const upAudioChnage = async () => {
    state.status = '正在处理...'
    const file = state.upaudio.files[0]
    if (!file) {
      ElMessage.error('请选择录音文件')
      return
    }
    const res = await recorder.getResult(file)
    const items = res.data[0]?.sentence_info
    state.url = res.data[0]?.url
    if (items) {
      state.speechItems = items.map(item => ({
        name: `说话人${item.spk}`,
        spk: item.spk,
        text: item.text,
      }))
    }
    state.status = ''
  }

  const upload = () => {
    state.upaudio.click()
  }

  const clean = () => {
    state.status = ''
    state.prompt = ''
    state.speechItems = []
    state.result = ''
    state.url = ''
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
  .speech-box {
    width: 49.5%;
    height: 100%;
    border: 1px solid #e5e6eb;
    border-radius: 10px;
    padding: 10px;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .toolbar .right {
    display: flex;
    align-items: center;
  }

  .toolbar .left {
    display: flex;
    align-items: center;
  }

  .type {
    width: 106px;
    height: 36px;
    background: url('@/assets/images/speech-type.png') no-repeat center center / 100% 100%;
    cursor: pointer;
  }

  .type-list {
    transform: translate(0, 65%);
    position: fixed;
    border: 1px solid #ebebeb;
    border-radius: 10px;
    padding: 5px;
    background: #ffffff;
  }

  .type-list .item {
    display: flex;
    align-items: center;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 10px;
  }

  .type-list .item:hover {
    background: #f5f5f5;
  }

  .type-list .icon {
    width: 16px;
    height: 16px;
    margin-right: 10px;
  }

  .type-list .icon.icon-mr {
    background: url('@/assets/images/icon-mr.png') no-repeat center center / 100% 100%;
  }

  .type-list .icon.icon-custom {
    background: url('@/assets/images/icon-custom.png') no-repeat center center / 100% 100%;
  }

  .type-list .icon.icon-clean {
    background: url('@/assets/images/icon-clean.png') no-repeat center center / 100% 100%;
  }

  .customize {
    width: 106px;
    height: 36px;
    background: url('@/assets/images/customize.png') no-repeat center center / 100% 100%;
    cursor: pointer;
    margin-left: 10px;
  }

  .rename {
    width: 122px;
    height: 36px;
    background: url('@/assets/images/speech-rename.png') no-repeat center center / 100% 100%;
    cursor: pointer;
  }

  .save {
    width: 106px;
    height: 36px;
    background: url('@/assets/images/save-audio.png') no-repeat center center / 100% 100%;
    cursor: pointer;
    margin-left: 10px;
  }

  .upload {
    width: 106px;
    height: 36px;
    background: url('@/assets/images/up-audio.png') no-repeat center center / 100% 100%;
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

  .speech.active {
    width: 23px;
    height: 23px;
    background-image: url('@/assets/images/icon-speech-active.png');
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

  .speech-list {
    border-top: 1px solid #e5e6eb;
    margin-top: 10px;
    overflow: auto;
    height: 230px;
  }

  .speech-list .item {
    padding: 0 10px;
    margin-top: 2px;
  }

  .speech-list .name {
    color: red;
  }

  .speech-list .content {
    color: #86909c;
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
