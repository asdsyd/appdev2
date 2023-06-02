<template>
  <user-nav-bar />

  <form @submit.prevent="HandleSubmit()">
    <div>
      <h1 class="form-label container mt-4">Welcome back! Please login to continue...</h1>
    </div>
    <div v-if="err" class="alert alert-danger " role="alert">
      {{ err }}
    </div>
    <div class="mt-4 mb-3 col-3 container ">
      <input class="container col-3 form-control rounded-pill " type="text" v-model="details.username" placeholder="" />
    </div>
    <div class="mt-3 mb-3 col-3 container">
      <input class="container col-3 form-control rounded-pill" type="password" v-model="details.password" placeholder="Password" />
    </div>
    <div class="mt-3 col-3 container">
      <input class="container mb-3 px-4 btn btn-outline-primary rounded-pill" type="submit" value="Login" placeholder="Login" />
    </div>
    <h6 class="text">New to ticketshow? </h6> <router-link :to="'/user/register'" class="link-offset-1-hover text-decoration-none">register </router-link>

  </form>


  <user-bottom-nav-bar />
</template>

<script setup>

import UserNavBar from "@/views/UserNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";


</script>