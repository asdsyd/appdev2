
<template>

  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Username's Dashboard</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Summary</a>
          </li>
        </ul>
        <button class="btn btn-outline-success" type="submit">Logout</button>
      </div>
    </div>
  </nav>
  <div>
    <form class="m-3" @submit.prevent="handleclick">
      <!-- 2 column grid layout with text inputs for the first and last names -->
      <div class="row mb-4">
        <div class="col-4">
          <div class="form-outline">
            <input type="text" id="form6Example1" class="form-control" v-model="venue.name"/>
            <label class="form-label" for="form6Example1">Venue name</label>
          </div>
        </div>
        <div class="col-2 form-outline mb-4">
          <input type="number" id="form6Example3" class="form-control" v-model="venue.capacity"/>
          <label class="form-label" for="form6Example3">Capacity</label>
        </div>
      </div>

      <!-- Text input -->

      <!-- Text input -->
      <div class="col-6 form-outline mb-4">
        <input type="text" id="form6Example4" class="form-control" v-model="venue.place"/>
        <label class="form-label" for="form6Example4">Place</label>
      </div>

      <!-- Email input -->
      <div class="col-6 form-outline mb-4">
        <select class="form-select" v-model="venue.location">
          <option>Hyderabad</option>
          <option>Delhi</option>
          <option>Mumbai</option>
          <option>Chennai</option>
          <option>Kolkata</option>
          <option>Bangalore</option>
        </select>
        <label class="form-label" for="form6Example5">Location</label>
      </div>
      <button type="submit" class="left col-2 btn btn-primary ">Save</button>


      <!-- Submit button -->
    </form>
  </div>

</template>


<script setup>

import {reactive} from "vue";
import axios from "axios";

const venue = reactive({
  name:'',
  capacity:0,
  place:'',
  location:''
})
const handleclick = ()=>{
console.log(venue)
  axios.post('http://localhost:8000/admin/createVenue',venue).then(res=>console.log(res.data)).catch(err=>console.log(err.response.data))
}

</script>


<style>

.left {
  translate: -250px 0px;
}

</style>