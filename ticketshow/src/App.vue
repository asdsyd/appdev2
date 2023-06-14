<template  >
  <router-view />
</template>
<script setup>
</script>
<style>
.blurrr{
  filter: blur(10px);
  opacity: 0.6;
  background-color: rgba(0, 0, 0, 0.1);
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.blur {
  filter: blur(4px); /* Apply the desired blur effect */
  pointer-events: none; /* Disable interaction with the blurred content */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
