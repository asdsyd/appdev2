<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
<div class="container-fluid">
  <h1 class="display-6 text-black-1000 cust" >{{username}}'s Dashboard</h1>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
      <li class="nav-item">
        <router-link class="m-2 lead text-black-1000 text-decoration-none" :to="'/admin/' + $store.state.admin.username">Home</router-link>
      </li>
      <li class="nav-item">
        <router-link class="m-2 lead text-black-1000 text-decoration-none" :to="'/adminexports'">exports</router-link>
      </li>
      <li :hidden="isSummary" class="nav-item me-2">
        <router-link class=" lead text-black-1000 text-decoration-none" :to="'/admin/' + $store.state.admin.username +'/AdminSummary'">Summary</router-link>
      </li>
    </ul>
    <button class="btn btn-outline-success" type="submit" @click="Adminlogout">Logout</button>
  </div>
</div>
</nav>
</template>
<script setup>
import { computed ,watchEffect} from 'vue';
import store from '@/store';
import router from '@/router';

const username = computed(()=>store.state.admin.username)
const Adminlogout = () => {
  store.commit("removeadmin");
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