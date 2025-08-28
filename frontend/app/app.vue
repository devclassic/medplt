<template>
  <NuxtLayout :name="state.layout">
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
  const state = reactive({
    layout: 'main',
  })

  const route = useRoute()

  watchEffect(() => {
    if (route.path === '/' || route.path === '/login') {
      state.layout = 'empty'
    } else {
      state.layout = 'main'
    }
  })
</script>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
</style>
