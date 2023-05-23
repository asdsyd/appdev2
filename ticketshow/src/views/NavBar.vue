<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
<div class="container-fluid">
  <h1 class="display-6 text-black-1000 text-uppercase" >{{$store.state.user.username}}'s Dashboard</h1>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
      <li class="nav-item">
        <router-link class="m-2 lead text-black-1000 text-decoration-none" :to="'/admin/' + $store.state.user.username">Home</router-link>
      </li>
      <li :hidden="isSummary" class="nav-item">
        <router-link class=" lead text-black-1000 text-decoration-none" :to="'/admin/' + $store.state.user.username +'/AdminSummary'">Summary</router-link>
      </li>
    </ul>
    <button class="btn btn-outline-success" type="submit">Logout</button>
  </div>
</div>
</nav>
</template>
<script setup>
defineProps({
  isSummary:Boolean
})
</script>