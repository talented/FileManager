// import "../node_modules/ag-grid-community/dist/styles/ag-grid.css";
// import "../node_modules/ag-grid-community/dist/styles/ag-theme-balham.css";

import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import BootstrapVue from 'bootstrap-vue'
import store from './store'

Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

axios.defaults.baseURL = 'http://localhost:8001'
axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'

new Vue({
  el: '#app',
  store,
  components: {
    'django': App
  }
})
