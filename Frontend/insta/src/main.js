import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false
Vue.use(BootstrapVue)



new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
