import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import '/@modules/element-plus/lib/theme-chalk/index.css'

const app = createApp(App)

app.use(ElementPlus, { size: 'small', zIndex: 3000, })
const components = [
]
components.forEach(component => {
  app.component(component.name, component)
})

app.use(router)
app.use(store)
app.mount('#app')
