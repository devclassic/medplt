export default defineNuxtRouteMiddleware(to => {
  if (
    to.path === '/' ||
    to.path === '/login' ||
    to.path === '/login/' ||
    to.path === '/admin/login' ||
    to.path === '/admin/login/'
  ) {
    setPageLayout('empty')
  } else if (to.path.startsWith('/admin')) {
    setPageLayout('admin')
  } else {
    setPageLayout('main')
  }
})
