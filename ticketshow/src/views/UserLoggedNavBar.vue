

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <span class="">
        <img src="../assets/ticketshow-logo.png" class="navbar-brand img-fluid img-thumbnail card-img" alt="TicketShow Logo" id="logo"/>
      <span class="pe-5">Welcome {{ $store.state.user.username }}</span>
      </span>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item mx-2">
            <router-link :to="'/'" class="nav-link active" aria-current="page" >Home</router-link>
          </li>

          <li class="nav-item dropdown mx-2">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Explore
            </a>
            <ul class="dropdown-menu">
              <li><router-link :to="'/'+ $store.state.user.username + '/profile'" class="dropdown-item" href="#">My Profile</router-link></li>
              <li><router-link :to="'/'+ $store.state.user.username + '/bookings'" class="dropdown-item">My Bookings</router-link></li>
              <li><router-link :to="'/admin/dashboard'" class="dropdowfn-item">Admin tools</router-link></li>
              <li><hr class="dropdown-divider"></li>
              <li><router-link :to="'/user/login'" class="dropdown-item" href="#">Rate movie</router-link></li>
            </ul>
          </li>
          <li class="nav-item mx-2">
            <a class="nav-link disabled">Offers</a>
          </li>
          <li class="nav-item mx-2">
            <router-link :to="'/about'" class="nav-link" >About</router-link>
          </li>
        </ul>
        <div class="container">
          <button class="btn btn-outline-success rounded-pill" type="submit" @click="logout">Logout</button>

        </div>
      </div>
    </div>
  </nav>
</template>
<script setup>
import store from '@/store';
import router from '@/router';
const logout = () => {
  store.commit("removeuser");
  router.push("/user/login");
};
</script>
<style scoped>

</style>