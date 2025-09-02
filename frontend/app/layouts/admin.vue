<template>
  <el-container>
    <el-aside class="aside">
      <el-menu
        active-text-color="#ffd04b"
        background-color="#545c64"
        default-active="1"
        text-color="#fff"
        class="menu">
        <el-menu-item index="1">
          <el-icon><house /></el-icon>
          <span>首页</span>
        </el-menu-item>
        <el-menu-item index="2">
          <el-icon><user /></el-icon>
          <span>用户管理</span>
        </el-menu-item>
        <el-menu-item index="3">
          <el-icon><document /></el-icon>
          <span>历史记录</span>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><money /></el-icon>
          <span>充值管理</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-main>
      <slot />
    </el-main>
  </el-container>
</template>

<style>
  body {
    background: #f5f5f5;
  }
</style>

<style scoped>
  .aside {
    width: 200px;
    min-height: 100vh;
    background: #545c64;
  }

  .menu {
    width: 100%;
    border-right: 1px solid #545c64;
  }
</style>
