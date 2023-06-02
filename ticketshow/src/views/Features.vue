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

  <h1>Some features of Ticketshow</h1>
  <div>
    Movie Search: Allow users to search for movies by title, genre, or actors.
  </div>
  <div>
    Movie Details: Provide detailed information about each movie, including synopsis, cast, director, release date, duration, and user ratings.
  </div>
  <div>
    Showtime Selection: Allow users to select the desired showtime for a movie, including date and time.
  </div>
  <div>
    Multiple Theater Support: Extend the app to support multiple theaters or cinema chains, allowing users to choose their preferred location.
  </div>
  <div>
    Booking Confirmation: Provide users with a confirmation screen summarizing their booking details before completing the purchase.
  </div>
  <div>
    Admin Panel: Develop an admin panel to manage movie listings, showtimes, seating arrangements, and user reviews/ratings.
  </div>


  <user-bottom-nav-bar/>
</template>
<script setup>
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
</script>