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
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <router-link :to="'/about'" class="nav-link" >About</router-link>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Dropdown
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <router-link :to="'/user/login'" class="btn btn-outline-success rounded-pill" type="submit">Login/Register</router-link>
        </form>
      </div>
    </div>
  </nav>
  <div class="container center">
    <h1 class="display-1">Welcome to <span class="rounded-pill px-4 custom-border">TicketShow</span></h1>
  </div>
  <div>
    <p class="container">Welcome to Ticket Show, the ultimate movie booking app that brings the magic of cinema right to your fingertips. With our user-friendly platform, you can easily browse, book, and enjoy your favorite movies with just a few taps.

      At Ticket Show, we understand the thrill of catching the latest blockbuster or experiencing the enchantment of an indie gem. That's why we have designed our app to provide you with a seamless and hassle-free movie booking experience. Whether you're a cinephile seeking the next cinematic masterpiece or simply looking for a fun night out, Ticket Show has got you covered.</p>
  </div>
  <div class="container center">
    <h1 class="display-5">Under construction. come back soon...</h1>
  </div>
</template>
<style>
#logo{
  width:12%
}

.custom-border {
  --border-size: 3px;
  --border-angle: 0turn;
  width: 60vmin;
  height: 50vmin;
  background-image: conic-gradient(from var(--border-angle), #213, #112 50%, #213), conic-gradient(from var(--border-angle), transparent 20%, #08f, #f03);
  background-size: calc(100% - (var(--border-size) * 2)) calc(100% - (var(--border-size) * 2)), cover;
  background-position: center center;
  background-repeat: no-repeat;
  animation: bg-spin 3s linear infinite;
}

@keyframes bg-spin {
  to {
    --border-angle: 1turn;
  }
}


</style>
<script setup>
import NavBar from "@/views/NavBar.vue";
import UserLogin from "@/views/UserLogin.vue";
</script>
