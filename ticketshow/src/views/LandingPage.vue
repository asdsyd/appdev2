<template>
  <user-nav-bar />
<!--Page content-->
  <div class="container center mt-4">
    <h1 class="display-1">Welcome to <span class="rounded-pill px-4 custom-border text-light"
    style="background-color:coral">TicketShow</span></h1>
  </div>
  <div>
    <p class="container fs-5 mt-4 fw-semibold">Ticket Show is the ultimate movie booking app that brings the magic of cinema right to your fingertips. With our user-friendly platform, you can easily browse, book, and enjoy your favorite movies with just a few taps.

      At Ticket Show, we understand the thrill of catching the latest blockbuster or experiencing the enchantment of an indie gem. That's why we have designed our app to provide you with a seamless and hassle-free movie booking experience. Whether you're a cinephile seeking the next cinematic masterpiece or simply looking for a fun night out, Ticket Show has got you covered.</p>
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
import UserNavBar from "@/views/UserNavBar.vue";
</script>
