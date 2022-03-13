import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from 'axios'
import Global from "./components/Global.vue"
import { Vue } from 'vue-class-component'

// 登录请求预处理，存储cookie
axios.defaults.withCredentials = true
// Vue.prototype.$Global = Global

const app = createApp(App)
app.use(store).use(router).use(ElementPlus).mount('#app')
app.config.globalProperties.$axios = axios