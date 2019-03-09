<template>
    <header class="head">
        <b-navbar type="dark" variant="primary" toggleable>
            <b-navbar-brand href="#">
              <font-awesome-icon icon="tasks"/>&nbsp; &nbsp; File Manager</b-navbar-brand>
            <b-navbar-nav class="ml-auto">
              <router-link tag='li' :to="{ name: 'cutecat'}">
              <b-nav-item >Download</b-nav-item>
              </router-link>
            </b-navbar-nav>
        </b-navbar>
    </header>
</template>
<script>
export default{
  data () {
    return {
}
  }
}
</script>
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Roboto+Condensed')
  .head {
    font-family: 'Roboto Condensed', sans-serif;
  }
</style>
