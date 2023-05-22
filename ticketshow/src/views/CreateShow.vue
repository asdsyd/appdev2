
<template>
  <NavBar></NavBar>
  <div>
    <h1>{{ header }}</h1>
  </div>
  <div>
    <!--    creating create-show form-->
    <form class="m-3" @submit.prevent="handleSubmit">
      <div class="row mb-4">
        <div class="col-4">
          <div class="form-outline">
            <input type="text" id="form6Example1" class="form-control" v-model="showName" />
            <label class="form-label" for="form6Example1">Show name</label>
          </div>
        </div>

        <div class="col-2 form-outline mb-4">
          <select class="form-select" v-model="rating">
            <option disabled value="">Please select one</option>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </select>
          <label>Rating</label>
        </div>

        <div class="container">
          <label>Start time</label>
          <input type="time" class="align-self-auto" v-model="startTime" />
          <label>End time</label>
          <input type="time" class="align-self-auto" v-model="endTime">
        </div>
      </div>

      <div class="checkboxes form-check-inline">
        <h4>Select Tags:</h4>
        <label>Thriller</label>
        <input class="" type="checkbox" value="thriller" v-model="tags" />

        <label>Action</label>
        <input type="checkbox" value="action" v-model="tags" />

        <label>Comedy</label>
        <input type="checkbox" value="comedy" v-model="tags" />

        <label>Superhero</label>
        <input type="checkbox" value="superhero" v-model="tags" />

        <label>Animation</label>
        <input type="checkbox" value="animation" v-model="tags" />
      </div>

      <div class="col-6 form-outline mb-4">
        <input type="number" class="col-4 form-control" v-model="ticketPrice">
        <label class="form-label" for="form6Example5">Ticket Price</label>
      </div>

      <button type="submit" class="left col-2 btn btn-primary " >Save</button>


      <!-- Submit button -->
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from "axios";
import NavBar from "@/views/NavBar.vue";

const header = ref('Create a Show')
const showName = ref("")
const rating = ref([])
const startTime = ref("")
const endTime = ref("")
const tags = ref([])
const ticketPrice = ref(0)
const handleSubmit=()=>{
  const show = {
    showName,
    rating,
    startTime,
    endTime,
    tags,
    ticketPrice
  }
  axios.post('http://localhost:8000/admin/Venue/CreateShow', show).then(res=>console.log(res.data)).catch(error=>console.log(error))
}
</script>


<style>
.left {
  translate: -250px 0px;
}
.checkboxes {
  text-align:center;
}

.checkboxes input{
  margin: 0px 20px 0px 0px;
}

.checkboxes label{
  margin: 0px 20px 0px 3px;
}

</style>