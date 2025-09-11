<template>
  <div spellcheck="false" class="box">
    <div class="left"></div>
    <div class="right">
      <div class="login-box">
        <div class="title">端点AI医疗数字平台</div>
        <div class="form">
          <div class="input-box">
            <div class="label">
              <span class="icon icon-user"></span>
              <span>账号</span>
            </div>
            <input type="text" class="input" />
          </div>
          <div class="input-box">
            <div class="label">
              <span class="icon icon-pass"></span>
              <span>密码</span>
            </div>
            <input type="text" class="input" />
          </div>
          <div class="input-box">
            <div class="label">
              <span class="icon icon-pass"></span>
              <span>验证码</span>
            </div>
            <div class="code-box">
              <input type="text" class="input" />
              <img src="@/assets/images/login-code.png" />
            </div>
          </div>
          <div @click="login" class="submit">登录</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  const router = useRouter()

  const login = () => {
    router.push('/')
  }
</script>

<style scoped>
  .box {
    width: 1920px;
    height: 100%;
    position: fixed;
    display: flex;
    overflow: auto;
  }

  .left {
    width: 50%;
    height: 100%;
    background: url('@/assets/images/login-left-bg.png') no-repeat center center / 100% 100%;
  }

  .right {
    width: 50%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .login-box {
    width: 590px;
    line-height: 1;
  }

  .title {
    font-size: 65px;
    color: #011f3c;
    font-weight: bold;
  }

  .form {
    margin-top: 50px;
  }

  .input-box {
    margin-top: 30px;
  }

  .label {
    font-size: 16px;
    color: #888e9e;
  }

  .label span {
    display: inline-block;
    vertical-align: middle;
  }

  .icon {
    width: 17px;
    height: 18px;
    margin: 0 10px 0 5px;
  }

  .icon-user {
    background: url('@/assets/images/login-icon-user.png') no-repeat center center / 100% 100%;
  }

  .icon-pass {
    background: url('@/assets/images/login-icon-pass.png') no-repeat center center / 100% 100%;
  }

  .icon-pass {
    background: url('@/assets/images/login-icon-pass.png') no-repeat center center / 100% 100%;
  }

  .input {
    width: 100%;
    height: 64px;
    border: 1px solid #ececf2;
    outline: none;
    background: #f9fbfc;
    border-radius: 10px;
    font-size: 16px;
    padding: 0 20px;
    margin-top: 15px;
  }

  .code-box {
    position: relative;
  }

  .code-box img {
    position: absolute;
    width: 147px;
    height: 54px;
    top: 20px;
    right: 5px;
    cursor: pointer;
  }

  .submit {
    height: 75px;
    line-height: 75px;
    text-align: center;
    font-size: 22px;
    color: #fff;
    background: #13a5c7;
    margin-top: 60px;
    border-radius: 10px;
    cursor: pointer;
  }
</style>
