<script setup>

</script>

<template>
  <!--  Bottom Navbar-->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-bottom">
    <div class="container-fluid">
      <span>
        <router-link to="'/'">
      <img src="../assets/ticketshow-logo.png" class="navbar-brand img-fluid img-thumbnail logo-bottom" alt="TicketShow Logo"/>
        </router-link>
      <router-link :to="'/'">
      <span class="navbar-brand disabled" href="#">TicketShow</span>
      </router-link>
      </span>
      <ul class="nav nav-tabs justify-content-center">
        <li class="nav-item nav-tabs">
          <router-link :to="'/about'" class="nav-link text-decoration-none" aria-current="page" >About</router-link>
        </li>
        <li class="nav-item nav-tabs">
          <router-link :to="'/features'" class="nav-link text-decoration-none" >Features</router-link>
        </li>
        <li class="nav-item nav-tabs">
          <router-link :to="'/'" class="nav-link text-decoration-none" >Contact Us</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>

</style>