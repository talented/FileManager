<template>
    <header>
        <b-navbar type="dark" variant="primary" toggleable>
            <b-navbar-brand href="#">File Manager</b-navbar-brand>
            <b-navbar-nav class="ml-auto">
              <!-- <router-link tag='li' :to="{ name: 'home'}">
                <b-nav-item>File Manager</b-nav-item>
              </router-link> -->

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

</style>
