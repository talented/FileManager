<template>
  <div id="app">
    <Header></Header>
    <Home></Home>
  </div>
</template>

<script>
import Header from "./components/Header";
import Home from "./components/Home";

export default {
  name: "app",
  components: {
    Header,
    Home
  }
};
</script>

<style>
#app {
  font-family: "Questrial";
}
</style>
