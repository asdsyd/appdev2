<template>

  <nav class="navbar navbar-expand-lg bg-body-tertiary">
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

  <div class="my-3 container">
    <div class=" mb-3  display-3 rounded-pill border border-success ">About Us</div>

    <figure class="text-center mt-4">
      <blockquote class="blockquote">
        <p>Step into a world of magic and adventure. Your ticket to unforgettable cinematic journeys.</p>
      </blockquote>
      <figcaption class="blockquote-footer">
        Yours one and only <cite title="Source Title">booking app</cite>
      </figcaption>
    </figure>

    <p class="container mt-3"><img src="../assets/ticketshow-logo.png" class="" id="paraPic"></p> <p class="lead container">TicketShow
    is a movie booking app to meet our customer's request to reserve seats for a show in a theatre.</p> <p class="container pb-5"> Whether you're planning a solo movie night or a group outing with friends, Ticket Show is the ultimate companion for all your movie booking needs. Download our app today and embark on a cinematic journey like never before.

      Lights, camera, action! Welcome to Ticket Show, where your movie experience begins.</p>
  </div>

  <UserBottomNavBar/>
</template>
<style>
#paraPic{
  width: 50%;
}
</style>
<script setup>
// @ is an alias to /src

import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
</script>
