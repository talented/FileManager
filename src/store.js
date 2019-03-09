import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex, axios)

export default new Vuex.Store ({
  state: {
    rowData: []
  },
  actions: {

    loadFiles ({ commit }) {
      axios
           .get('api/files/')
           .then(data => {
             let rowData = data.data
             commit('SET_FILES', rowData)
           })
           .catch(error => {
             console.log(error)
           })
    }
  },
  mutations: {
    SET_FILES (state, files) {
      state.rowData = files
    }
  }
})
