<template>
  <div class="wrap">
    <div class="title">语音表单</div>
    <div class="box">
      <div class="btn-box">
        <div @click="asr" class="btn btn1">{{ state.btn1Text }}</div>
        <div @click="reset" class="btn btn2">重置表单</div>
        <input
          type="file"
          ref="upfile"
          @change="upfileChange"
          style="width: 0; height: 0; opacity: 0" />
        <div @click="upload" class="btn btn4">语音上传</div>
        <div class="status">{{ state.status }}</div>
      </div>
      <div class="info1">
        <div class="info1-title">基本信息</div>
        <div class="form1">
          <div class="row">
            <div class="col">
              <div>姓名：</div>
              <input type="text" placeholder="请输入" v-model="state.form.姓名" />
            </div>
            <div class="col">
              <div>就诊时间：</div>
              <input type="text" placeholder="请输入" v-model="state.form.就诊时间" />
            </div>
          </div>
          <div class="row">
            <div class="col">
              <div>性别：</div>
              <input type="text" placeholder="请输入" v-model="state.form.性别" />
            </div>
            <div class="col">
              <div class="label">科室：</div>
              <input type="text" placeholder="请输入" v-model="state.form.科室" />
            </div>
          </div>
          <div class="row">
            <div class="col">
              <div>年龄：</div>
              <input type="text" placeholder="请输入" v-model="state.form.年龄" />
            </div>
            <div class="col">
              <div>接诊医生：</div>
              <input type="text" placeholder="请输入" v-model="state.form.接诊医生" />
            </div>
          </div>
          <div class="row">
            <div class="col">
              <div>电话：</div>
              <input type="text" placeholder="请输入" v-model="state.form.电话" />
            </div>
            <div class="col">
              <div class="label">地址：</div>
              <input type="text" placeholder="请输入" v-model="state.form.地址" />
            </div>
          </div>
        </div>
      </div>
      <div class="info2">
        <div class="info2-title">
          主要信息
          <div @click="optimize" class="btn btn3">{{ state.btn3Text }}</div>
        </div>
        <div class="form2">
          <div class="item">
            <div class="h">主诉</div>
            <textarea placeholder="主诉" v-model="state.form.主诉"></textarea>
          </div>
          <div class="item">
            <div class="h">现病史</div>
            <textarea placeholder="现病史" v-model="state.form.现病史"></textarea>
          </div>
          <div class="item">
            <div class="h">既往史</div>
            <textarea placeholder="既往史" v-model="state.form.既往史"></textarea>
          </div>
          <div class="item">
            <div class="h">过敏史</div>
            <textarea placeholder="过敏史" v-model="state.form.过敏史"></textarea>
          </div>
          <div class="item">
            <div class="h">家族史</div>
            <textarea placeholder="家族史" v-model="state.form.家族史"></textarea>
          </div>
          <div class="item">
            <div class="h">体格检查</div>
            <textarea placeholder="体格检查" v-model="state.form.体格检查"></textarea>
          </div>
          <div class="item">
            <div class="h">专科检查</div>
            <textarea placeholder="专科检查" v-model="state.form.专科检查"></textarea>
          </div>
          <div class="item">
            <div class="h">辅助检查</div>
            <textarea placeholder="辅助检查" v-model="state.form.辅助检查"></textarea>
          </div>
          <div class="item">
            <div class="h">初步诊断</div>
            <textarea placeholder="初步诊断" v-model="state.form.初步诊断"></textarea>
          </div>
          <div class="item">
            <div class="h">鉴别诊断</div>
            <textarea placeholder="鉴别诊断" v-model="state.form.鉴别诊断"></textarea>
          </div>
          <div class="item">
            <div class="h">治疗目的</div>
            <textarea placeholder="治疗目的" v-model="state.form.治疗目的"></textarea>
          </div>
          <div class="item">
            <div class="h">健康教育</div>
            <textarea placeholder="健康教育" v-model="state.form.健康教育"></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  const state = reactive({
    status: '',
    btn1Text: '开始收音',
    btn3Text: '信息优化',
    form: {
      姓名: '',
      性别: '',
      年龄: '',
      电话: '',
      就诊时间: '',
      科室: '',
      接诊医生: '',
      地址: '',
      主诉: '',
      现病史: '',
      既往史: '',
      过敏史: '',
      家族史: '',
      体格检查: '',
      专科检查: '',
      辅助检查: '',
      初步诊断: '',
      鉴别诊断: '',
      治疗目的: '',
      健康教育: '',
    },
    upfile: useTemplateRef('upfile'),
  })

  const http = useAxios()
  const config = useRuntimeConfig()
  const recorder = useRecorder()

  let recording = ref(false)

  const fillForm = async (audio = null) => {
    const result = await recorder.getResult(audio)
    const text = result.data[0]?.text
    const url = config.public.BASE_URL + '/api/client/asr/chat'
    const prompt = `<内容>${text}</内容>

  请你分析<内容>中内容，并提取其中的关键信息，以 JSON 的形式输出，输出的 JSON 需遵守以下的格式：

  {
    "姓名": <姓名>,
    "性别": <性别>,
    "年龄": <年龄>,
    "电话": <电话>,
    "就诊时间": <就诊时间>,
    "科室": <科室>,
    "接诊医生": <接诊医生>,
    "地址": <地址>,
    "主诉": <主诉>,
    "现病史": <现病史>,
    "既往史": <既往史>,
    "过敏史": <过敏史>,
    "家族史": <家族史>,
    "体格检查": <体格检查>,
    "专科检查": <专科检查>,
    "辅助检查": <辅助检查>,
    "初步诊断": <初步诊断>,
    "鉴别诊断": <鉴别诊断>,
    "治疗目的": <治疗目的>,
    "健康教育": <健康教育>
  }

  如果<内容>中没有相关信息，则输出空字符串。
  输出的 JSON 中，所有的字段都必须包含在 JSON 中，不能省略。`
    const res = await http.post(url, { prompt })
    const data = res.data.data.answer
      .replace(/<think>[\s\S]*?<\/think>/g, '')
      .replace('```json', '')
      .replace('```', '')
    const json = JSON.parse(data)
    for (const key in state.form) {
      if (json[key]) {
        state.form[key] = json[key]
      }
    }
  }

  const asr = async () => {
    if (!recording.value) {
      state.status = '开始收音...'
      recorder.start(
        () => {
          state.status = '录音中...'
          recording.value = true
        },
        () => {
          state.status = '录音失败...'
          recording.value = false
        }
      )
    } else {
      state.status = '生成对话...'
      await fillForm()
      state.status = ''
      recording.value = false
    }
    state.btn1Text = state.btn1Text === '开始收音' ? '停止收音' : '开始收音'
  }

  const upload = async () => {
    state.upfile.click()
  }

  const upfileChange = async e => {
    const file = e.target.files[0]
    if (!file) {
      return
    }
    state.status = '上传处理中...'
    await fillForm(file)
    state.status = ''
  }

  const optimize = async () => {
    state.btn3Text = '优化中...'
    const url = config.public.BASE_URL + '/api/client/asr/chat'
    const keys = [
      '主诉',
      '现病史',
      '既往史',
      '过敏史',
      '家族史',
      '体格检查',
      '专科检查',
      '辅助检查',
      '初步诊断',
      '鉴别诊断',
      '治疗目的',
      '健康教育',
    ]
    for (const key in state.form) {
      const content = state.form[key]
      if (!keys.includes(key) || !content) {
        continue
      }
      const prompt = `<内容>${content}</内容>
<内容>为${key}。
你是一名专业医生，将医<内容>转化为标准医学表述，准确提取医患对话中的关键医疗信息，只优化最终结果，不提出意见，保持专业、客观的表述，你需要系统性地优化录音内容，消除所有口语化、模糊和带有语气词的表述，并使用精确、客观的医学术语进行规范记录，最终生成的语句需逻辑严谨、术语规范，符合医疗文书标准。`
      const res = await http.post(url, { prompt })
      const data = res.data.data.answer.replace(/<think>[\s\S]*?<\/think>/g, '')
      state.form[key] = data.trim()
    }
    state.btn3Text = '信息优化'
  }

  const reset = () => {
    state.form = {
      姓名: '',
      性别: '',
      年龄: '',
      电话: '',
      就诊时间: '',
      科室: '',
      接诊医生: '',
      地址: '',
      主诉: '',
      现病史: '',
      既往史: '',
      过敏史: '',
      家族史: '',
      体格检查: '',
      专科检查: '',
      辅助检查: '',
      初步诊断: '',
      鉴别诊断: '',
      治疗目的: '',
      健康教育: '',
    }
  }
</script>

<style scoped>
  .wrap {
    position: relative;
    height: 100%;
    overflow: auto;
  }

  .title {
    line-height: 1;
    font-size: 22px;
    color: #011f3c;
    padding: 30px 30px 25px 30px;
  }

  .box {
    padding: 0 30px;
  }

  .btn-box {
    display: flex;
  }

  .btn {
    width: 90px;
    text-align: center;
    height: 30px;
    line-height: 30px;
    font-size: 15px;
    color: #ffffff;
    background: #00a8ff;
    border-radius: 5px;
    cursor: pointer;
  }

  .btn2,
  .btn4 {
    margin-left: 20px;
  }

  .btn3 {
    position: absolute;
    top: -6px;
    left: 110px;
  }

  .status {
    margin-left: 20px;
    color: #cccccc;
  }

  .info1 {
    margin-top: 20px;
  }

  .info1-title {
    line-height: 1.1;
    padding-left: 10px;
    border-left: 2px solid #0080c2;
  }

  .info2 {
    margin-top: 20px;
    position: relative;
  }

  .info2-title {
    line-height: 1.1;
    padding-left: 10px;
    border-left: 2px solid #0080c2;
  }

  .form1 {
    margin-top: 20px;
  }

  .row,
  .col {
    display: flex;
  }

  .row {
    justify-content: space-between;
    margin-bottom: 10px;
    padding-left: 10px;
  }

  .col {
    width: 49.5%;
  }

  .col .label {
    width: 80px;
    text-align: right;
  }

  .col input {
    border: 1px solid #c4c9ce;
    border-radius: 10px;
    padding: 0 10px;
    flex: 1;
  }

  .item {
    padding-left: 10px;
    margin-bottom: 10px;
  }

  .item textarea {
    width: 100%;
    border: 1px solid #c4c9ce;
    margin-top: 10px;
    border-radius: 10px;
    padding: 10px;
    height: 80px;
  }

  .h {
    text-align: center;
  }
</style>
