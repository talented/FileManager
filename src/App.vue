<template>
  <div id="app">
    <Header></Header>
    <Home></Home>
  </div>
</template>

<script>
import axios from 'axios'

import Header from './components/Header'
import Home from './components/Home'

export default {
  name: 'app',
  components: {
    Header,
    Home
  }
}
</script>

<style>
#app {
  /* text-align: center */
}
</style>
