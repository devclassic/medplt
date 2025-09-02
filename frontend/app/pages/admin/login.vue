<template>
  <div class="box">
    <el-card class="login-box">
      <template #header>登录</template>
      <el-form status-icon label-width="auto" class="demo-ruleForm">
        <el-form-item label="账户">
          <el-input type="text" autocomplete="off" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input type="password" autocomplete="off" />
        </el-form-item>
        <el-form-item label="验证">
          <el-input type="text" autocomplete="off" class="code-input" />
          <img src="@/assets/images/login-code.png" class="code" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button type="primary" class="login-btn">登录</el-button>
      </template>
    </el-card>
  </div>
</template>

<style>
  .el-card__body {
    padding-bottom: 0;
  }

  .el-form-item__content {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .el-form-item__content .code-input {
    width: 310px;
  }

  .el-form-item__content .code {
    width: 100px;
    height: 32px;
    cursor: pointer;
  }
</style>

<style scoped>
  .box {
    position: fixed;
    width: 100%;
    height: 100%;
    background: #f5f5f5;
  }

  .login-box {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 500px;
  }

  .login-btn {
    width: 100%;
  }
</style>
