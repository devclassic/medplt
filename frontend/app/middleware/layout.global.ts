export default defineNuxtRouteMiddleware(to => {
  if (to.path === '/' || to.path === '/login' || to.path === '/login/') {
    setPageLayout('empty')
  } else {
    setPageLayout('main')
  }
})
