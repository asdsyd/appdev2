<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
<div class="container-fluid">
  <h1 class="display-6 text-black-1000 cust" >{{$store.state.user.username}}'s Dashboard</h1>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
      <li class="nav-item">
        <router-link class="m-2 lead text-black-1000 text-decoration-none" :to="'/admin/' + $store.state.user.username">Home</router-link>
      </li>
      <li :hidden="isSummary" class="nav-item me-2">
        <router-link class=" lead text-black-1000 text-decoration-none" :to="'/admin/' + $store.state.user.username +'/AdminSummary'">Summary</router-link>
      </li>
      <li  class="nav-item">
        <router-link class=" lead text-black-1000 text-decoration-none" :to="'/'">User Login</router-link>
      </li>
    </ul>
    <form class="d-flex" role="search">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
    <button class="btn btn-outline-success" type="submit" @click="Adminlogout">Logout</button>
  </div>
</div>
</nav>
</template>
<script setup>
import store from '@/store';
import router from '@/router';
const Adminlogout = () => {
  store.commit("removeuser");
  router.push("/admin/login");
};
defineProps({
  isSummary:Boolean
})
</script>
<style scoped>
.cust{
  translate: 0px 5%;
}
</style>