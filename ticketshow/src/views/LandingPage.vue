<template>
  <nav v-if="!$store.state.user.accessToken" class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <span class="">
        <img src="../assets/ticketshow-logo.png" class="navbar-brand img-fluid img-thumbnail card-img" alt="TicketShow Logo" id="logo"/>
      <span class="pe-5">TicketShow</span>
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
              <li><router-link :to="'/user/login'" class="dropdown-item" href="#">Latest Movies</router-link></li>
              <li><router-link :to="'/user/login'" class="dropdown-item" href="#">Book a ticket</router-link></li>
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
          <router-link :to="'/user/login'" class="btn btn-outline-success rounded-pill" type="submit">Login/Register</router-link>

        </div>
      </div>
    </div>
  </nav>
  <user-logged-nav-bar v-else/>
<!--Page content-->
  <div class="container center mt-4">
    <h1 class="display-1">Welcome to <span class="rounded-pill px-4 custom-border bg-black text-light">TicketShow</span></h1>
  </div>
  <div>
    <p class="container fs-5 mt-4 fw-semibold">Welcome to Ticket Show, the ultimate movie booking app that brings the magic of cinema right to your fingertips. With our user-friendly platform, you can easily browse, book, and enjoy your favorite movies with just a few taps.

      At Ticket Show, we understand the thrill of catching the latest blockbuster or experiencing the enchantment of an indie gem. That's why we have designed our app to provide you with a seamless and hassle-free movie booking experience. Whether you're a cinephile seeking the next cinematic masterpiece or simply looking for a fun night out, Ticket Show has got you covered.</p>
  </div>
  <div class="container center pb-5">
    <h1 class="display-5">Under construction. come back soon...</h1>
  </div>

<UserBottomNavBar/>

</template>

<style>
#logo{
  width:12%
}
.logo-bottom{
  width: 8%;
}
</style>
<script setup>
import NavBar from "@/views/NavBar.vue";
import UserLogin from "@/views/UserLogin.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
</script>
