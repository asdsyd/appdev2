<template>
  <nav v-if="!$store.state.user.accessToken" class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container">
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

  <div class=" mb-3 container h1 rounded-pill border border-success ">Some features of Ticketshow</div>


  <div class="row row-cols-1 row-cols-md-3 g-5 container-fluid">
    <div class="col">
      <div class="card h-100">
        <img src="../assets/img.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Show Search</h5>
          <p class="card-text">Allows our users to search for movies by title, tags, or location.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <img src="../assets/img_1.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Show Details</h5>
          <p class="card-text">Provide detailed information about each movie, including synopsis, tags, ticket price, show timings and user ratings.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <img src="../assets/img_2.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Show Time Selection</h5>
          <p class="card-text">Allow users to select the desired showtime for a movie, including date and time.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <img src="../assets/img_3.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Multiple Venue Support</h5>
          <p class="card-text">Extend the app to support multiple theaters or cinema chains, allowing users to choose their preferred location.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <img src="../assets/img_4.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Booking Confirmation</h5>
          <p class="card-text">Provide users with a confirmation screen summarizing their booking details before completing the purchase.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card h-100">
        <img src="../assets/img_5.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Admin Panel and Tools</h5>
          <p class="card-text">Develop an admin panel to manage movie listings, showtimes, seating arrangements, and user reviews/ratings.</p>
        </div>
      </div>
    </div>

  </div>

  <user-bottom-nav-bar/>
</template>
<script setup>
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
</script>