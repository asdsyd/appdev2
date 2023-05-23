
<template>
  <NavBar></NavBar>
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

import { reactive, ref,onBeforeMount} from "vue";
import axios from "../axios";
import NavBar from "@/views/NavBar.vue";
import router from "@/router";
import {useStore} from "vuex";

const venue_Id = ref(router.currentRoute.value.params.Venue)
const store = useStore()
const venue = reactive({
  name:'',
  place:'',
  location:'',
  capacity:0,

})
onBeforeMount(()=>{
axios.get('/admin/'+ venue_Id.value+'/getVenuedata').then(res=>{
const {name,place,location,capacity} = res.data
  venue.name=name
  venue.place=place
  venue.location=location
  venue.capacity=capacity
}).catch(e=>{
  console.log(e)

})

})
const handleclick = ()=>{
  axios.post('/admin/'+ venue_Id.value +'/editVenue',venue).then(res=>router.push('/admin/'+store.state.user.username)).catch(err=>console.log(err))
}

</script>


<style>

.left {
  translate: -250px 0px;
}

</style>