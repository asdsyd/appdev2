<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <span class="">
        <img src="../assets/logo.png" class="navbar-brand img-fluid img-thumbnail card-img" alt="TicketShow Logo" id="logo"/>
      <span class="pe-5">TicketShow</span>
      </span>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link :to="'/'" class="nav-link active" aria-current="page" >Home</router-link>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <router-link :to="'/user/login'" class="btn btn-outline-success rounded-pill" type="submit">Login/Register</router-link>
        </form>
      </div>
    </div>
  </nav>

  <div class="my-3">
    <span class="px-5 mb-3  display-3 rounded-pill border border-success-subtle">About Us:</span>
    <p class="container mt-3"><img src="../assets/logo.png" class="img-thumbnail" id="paraPic"> TicketShow
    is a movie booking app to meet our customer's request to reserve seats for a show in a theatre. Whether you're planning a solo movie night or a group outing with friends, Ticket Show is the ultimate companion for all your movie booking needs. Download our app today and embark on a cinematic journey like never before.

      Lights, camera, action! Welcome to Ticket Show, where your movie experience begins.</p>
  </div>

</template>
<style>
#paraPic{
  width: 4%;
}
</style>
<script setup>
// @ is an alias to /src

</script>
