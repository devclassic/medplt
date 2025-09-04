import * as Icons from '@element-plus/icons-vue'

const RENAME: Record<string, string> = {
  filter: 'IconFilter',
  link: 'IconLink',
  menu: 'IconMenu',
  picture: 'IconPicture',
  select: 'IconSelect',
  switch: 'IconSwitch',
  view: 'IconView',
}

export default defineNuxtPlugin(({ vueApp }) => {
  Object.entries(Icons).forEach(([raw, comp]) => {
    const name = RENAME[raw] || raw
    vueApp.component(name, comp)
    vueApp.component(name.replace(/([A-Z])/g, '-$1').toLowerCase(), comp)
  })
})
