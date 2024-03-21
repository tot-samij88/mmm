import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from "./store";
import axios from "./axios.js";
import Chart from "chart.js";
import Chartick from "vue-chartkick";
import i18n from "@/plugins/i18n";
import Vuelidate from 'vuelidate'

Vue.use(Vuelidate)

Vue.config.productionTip = false

Vue.use(Chartick.use(Chart));

Vue.prototype.$http = axios;
Vue.config.performance = true;

new Vue({
  router,
  i18n,
  store,
  render: h => h(App)
}).$mount('#app')
