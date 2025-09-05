<template>
  <div spellcheck="false" class="box">
    <div class="center">
      <div class="title">端点AI医疗数字平台</div>
      <div class="link-box">
        <NuxtLink to="/speech">
          <img src="@/assets/images/index-link-1.png" />
        </NuxtLink>
        <NuxtLink to="/check">
          <img src="@/assets/images/index-link-2.png" />
        </NuxtLink>
        <NuxtLink to="/assist">
          <img src="@/assets/images/index-link-3.png" />
        </NuxtLink>
        <NuxtLink to="/image">
          <img src="@/assets/images/index-link-4.png" />
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
  .box {
    width: 1920px;
    height: 100%;
    background: url('@/assets/images/index-bg.png') no-repeat center center / 100% 100%;
    position: fixed;
  }

  .center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .title {
    font-size: 95px;
    color: #011f3c;
    font-weight: bold;
    text-align: center;
  }

  .link-box {
    width: 1480px;
    margin-top: 90px;
    display: flex;
    justify-content: space-between;
  }
</style>
