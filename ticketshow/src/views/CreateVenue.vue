
<template>
<NavBar></NavBar>
  <div>
    <form class="m-3" @submit.prevent="handleclick">
      <!-- 2 column grid layout with text inputs for the first and last names -->
      <h1 class="px-5 text-light display-4 rounded-pill show-pill-inside cust">
        Create Venue
      </h1>
      <div class="row mb-4">
        <div class="col-4">
          <div class="form-outline">
            <input type="text" id="form6Example1" class="form-control rounded-pill" v-model="venue.name"/>
            <label class="form-label" for="form6Example1">Venue name</label>
          </div>
        </div>
        <div class="col-2 form-outline mb-4">
          <input type="number" id="form6Example3" class="form-control rounded-pill" v-model="venue.capacity"/>
          <label class="form-label" for="form6Example3">Capacity</label>
        </div>
      </div>

      <!-- Text input -->

      <!-- Text input -->
      <div class="col-6 form-outline mb-4">
        <input type="text" id="form6Example4" class="form-control rounded-pill" v-model="venue.place"/>
        <label class="form-label" for="form6Example4">Place</label>
      </div>

      <!-- Email input -->
      <div class="col-6 form-outline mb-4">
        <select class="form-select rounded-pill" v-model="venue.location">
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
import axios from "../axios";
import NavBar from "@/views/NavBar.vue";
import router from "@/router";
import {useStore} from "vuex";

const store = useStore()
const venue = reactive({
  name:'',
  capacity:null,
  place:'',
  location:''
})
const handleclick = ()=>{
console.log(venue)
  axios.post('/admin/createVenue',venue).then(res=>setTimeout(()=>router.push('/admin/'+store.state.user.username,3000))).catch(err=>console.log(err))
}

</script>


<style>

.left {
  translate: -250px 0px;
}
.show-pill{
  display: flex;
  justify-content: center;

}
.show-pill-inside{
  background: rgb(2,0,36);

  background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%);

}

</style>