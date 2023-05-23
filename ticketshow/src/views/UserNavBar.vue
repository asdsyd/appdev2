<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <h1 class="display-5 text-light bg-success" >{{$store.state.user.username}}'s Dashboard</h1>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="btn btn-outline-primary text-decoration-none" :to="'/' + $store.state.user.username + '/profile'">Profile</router-link>
          </li>
          <li class="nav-item">
            <router-link class="btn btn-outline-primary text-decoration-none" :to="'/' + $store.state.user.username + '/bookings'" >Bookings</router-link>
          </li>
        </ul>
        <button class="btn btn-outline-success" type="submit">Logout</button>
      </div>
    </div>
  </nav>
</template>
<script setup>
</script>