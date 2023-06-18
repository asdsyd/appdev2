<script setup>

import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserNavBar from "@/views/UserNavBar.vue";
</script>

<template>
  <user-nav-bar/>
  <div class="container mt-4 ">
    <form class="d-flex" role="search">
      <input class="form-control me-2 rounded-pill" type="search" placeholder="Search for a Movie..." aria-label="Search">
      <button class="btn btn-outline-success rounded-pill" type="submit">Search</button>
    </form>
  </div>
  <user-bottom-nav-bar/>

</template>

<style scoped>

</style>