<script setup>

</script>

<template>
  <!--  Bottom Navbar-->
  <nav class="navbar navbar-dark navbar-expand-lg bg-dark fixed-bottom mt-4 ">
    <div class="container-fluid">
      <router-link class="text-decoration-none navbar-brand" to="/">
        <img src="../assets/ticketshow-logo.png" class=" img-thumbnail logo-bottom me-2" alt="TicketShow Logo"/>
        <span>TicketShow</span>
      </router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
        <ul class="navbar-nav mx-2">
          <li class="nav-item mx-2">
            <router-link :to="'/about'" class="nav-link text-decoration-none" aria-current="page" >About</router-link>
          </li>
          <li class="nav-item mx-2">
            <router-link :to="'/features'" class="nav-link text-decoration-none" >Features</router-link>
          </li>
          <li class="nav-item mx-2">
            <router-link :to="'/contactUs'" class="nav-link text-decoration-none" >Contact Us</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>


</template>

<style scoped>

</style>