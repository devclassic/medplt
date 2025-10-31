<template>
  <div spellcheck="false" class="box">
    <div class="side">
      <div class="side-box">
        <div>
          <img src="@/assets/images/logo.png" class="logo" />
        </div>
        <div class="menu-box">
          <NuxtLink to="/" class="menu-item">
            <span class="icon icon-home"></span>
            <span>首页</span>
          </NuxtLink>
          <NuxtLink to="/speech" class="menu-item" :class="{ active: path === '/speech' }">
            <span class="icon icon-speech"></span>
            <span>多人语音</span>
          </NuxtLink>
          <NuxtLink to="/form" class="menu-item" :class="{ active: path === '/form' }">
            <span class="icon icon-form"></span>
            <span>表单填写</span>
          </NuxtLink>
          <NuxtLink
            v-if="state.showMenu"
            to="/check"
            class="menu-item"
            :class="{ active: path === '/check' }">
            <span class="icon icon-check"></span>
            <span>辅助质控</span>
          </NuxtLink>
          <NuxtLink
            v-if="state.showMenu"
            to="/assist"
            class="menu-item"
            :class="{ active: path === '/assist' }">
            <span class="icon icon-chat"></span>
            <span>辅助诊疗</span>
          </NuxtLink>
          <NuxtLink
            v-if="state.showMenu"
            to="/image"
            class="menu-item"
            :class="{ active: path === '/image' }">
            <span class="icon icon-image"></span>
            <span>辅助影像</span>
          </NuxtLink>
          <NuxtLink to="/img" class="menu-item" :class="{ active: path === '/img' }">
            <span class="icon icon-img"></span>
            <span>图像分析</span>
          </NuxtLink>
          <NuxtLink to="/file" class="menu-item" :class="{ active: path === '/file' }">
            <span class="icon icon-file"></span>
            <span>文档分析</span>
          </NuxtLink>
          <NuxtLink to="/history" class="menu-item" :class="{ active: path === '/history' }">
            <span class="icon icon-history"></span>
            <span>历史记录</span>
          </NuxtLink>
          <NuxtLink to="/user" class="menu-item" :class="{ active: path === '/user' }">
            <span class="icon icon-user"></span>
            <span>个人中心</span>
          </NuxtLink>
        </div>
      </div>
      <div class="logout">
        <span class="icon icon-logout"></span>
        <span>退出登录</span>
      </div>
    </div>
    <div class="main">
      <div class="content">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup>
  import hotkeys from 'hotkeys-js'

  const state = reactive({
    showMenu: false,
  })

  onMounted(() => {
    state.showMenu = localStorage.getItem('showMenu') === 'true'
    hotkeys('alt+h', () => {
      const show = !state.showMenu
      state.showMenu = show
      localStorage.setItem('showMenu', show)
    })
  })

  const route = useRoute()
  const path = computed(() => route.path.replace(/\/$/, ''))

  useClientInit()
</script>

<style scoped>
  .box {
    width: 1920px;
    height: 100%;
    position: fixed;
    background: url('@/assets/images/bg.png') no-repeat center center / 100% 100%;
    display: flex;
  }

  .side {
    width: 300px;
    height: 100%;
    background: url('@/assets/images/side-bg.png') no-repeat center center / 100% 100%;
    position: relative;
  }

  .side-box {
    width: 240px;
    margin: 30px auto 0;
  }

  .logo {
    width: 145px;
    height: 35px;
    margin-left: 10px;
  }

  .menu-box {
    margin-top: 30px;
  }

  .menu-item {
    display: block;
    height: 50px;
    line-height: 45px;
    padding-left: 20px;
    margin-bottom: 20px;
    cursor: pointer;
    font-size: 16px;
    color: #092643;
  }

  .menu-item span {
    display: inline-block;
    vertical-align: middle;
  }

  .side .icon {
    width: 17px;
    height: 18px;
    margin-right: 10px;
  }

  .side .icon.icon-logout {
    background: url('@/assets/images/side-icon-logout.png') no-repeat center center / 100% 100%;
  }

  .logout {
    position: absolute;
    bottom: 30px;
    left: 30px;
    cursor: pointer;
    font-size: 16px;
    color: #092643;
  }

  .logout span {
    display: inline-block;
    vertical-align: middle;
  }

  .menu-item .icon.icon-home {
    background: url('@/assets/images/side-icon-home.png') no-repeat center center / 100% 100%;
  }

  .menu-item .icon.icon-speech {
    background: url('@/assets/images/side-icon-speech.png') no-repeat center center / 100% 100%;
  }

  .menu-item .icon.icon-form {
    background: url('@/assets/images/side-icon-form.png') no-repeat center center / 100% 100%;
  }

  .menu-item .icon.icon-check {
    background: url('@/assets/images/side-icon-check.png') no-repeat center center / 100% 100%;
  }

  .menu-item .icon.icon-chat {
    background: url('@/assets/images/side-icon-chat.png') no-repeat center center / 100% 100%;
  }

  .menu-item .icon.icon-image {
    background: url('@/assets/images/side-icon-image.png') no-repeat center center / 100% 100%;
  }

  .menu-item .icon.icon-img {
    background: url('@/assets/images/side-icon-img.png') no-repeat center center / 100% 100%;
  }

  .menu-item .icon.icon-file {
    background: url('@/assets/images/side-icon-file.png') no-repeat center center / 100% 100%;
  }

  .menu-item .icon.icon-history {
    background: url('@/assets/images/side-icon-history.png') no-repeat center center / 100% 100%;
  }

  .menu-item .icon.icon-user {
    background: url('@/assets/images/side-icon-user.png') no-repeat center center / 100% 100%;
  }

  .menu-item.active .icon.icon-speech {
    background: url('@/assets/images/side-icon-speech-active.png') no-repeat center center / 100%
      100%;
  }

  .menu-item.active .icon.icon-form {
    background: url('@/assets/images/side-icon-form-active.png') no-repeat center center / 100% 100%;
  }

  .menu-item.active .icon.icon-check {
    background: url('@/assets/images/side-icon-check-active.png') no-repeat center center / 100%
      100%;
  }

  .menu-item.active .icon.icon-chat {
    background: url('@/assets/images/side-icon-chat-active.png') no-repeat center center / 100% 100%;
  }

  .menu-item.active .icon.icon-image {
    background: url('@/assets/images/side-icon-image-active.png') no-repeat center center / 100%
      100%;
  }

  .menu-item.active .icon.icon-img {
    background: url('@/assets/images/side-icon-img-active.png') no-repeat center center / 100% 100%;
  }

  .menu-item.active .icon.icon-file {
    background: url('@/assets/images/side-icon-file-active.png') no-repeat center center / 100% 100%;
  }

  .menu-item.active .icon.icon-history {
    background: url('@/assets/images/side-icon-history-active.png') no-repeat center center / 100%
      100%;
  }

  .menu-item.active .icon.icon-user {
    background: url('@/assets/images/side-icon-user-active.png') no-repeat center center / 100% 100%;
  }

  .menu-item.active {
    color: #ffffff;
    background: url('@/assets/images/side-menu-bg.png') no-repeat center center / 100% 100%;
  }

  .main {
    width: 100%;
    padding: 20px;
  }

  .content {
    height: 100%;
    background: #ffffff;
    border-radius: 10px;
  }
</style>
