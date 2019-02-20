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
             // console.log('axios data', data.data)
             let rowData = data.data
             commit('SET_FILES', rowData)
             // console.log(rowData)
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



// axios
//    .get('api/files/')
//    .then(data => {
//      console.log('axios data', data.data)
//      this.posts = data.data
//      this.rowData = data.data
//
//    })
//    .catch(error => {
//      console.log(error)
//    })
