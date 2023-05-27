
<template>
  <NavBar></NavBar>
  <div class=" container show-pill" >
    <h1 class="px-5 text-light display-4 rounded-pill show-pill-inside">{{ header }}</h1>
  </div>
  <div class="outer">
    <!--    creating create-show form-->
    <form class="m-3 custom" @submit.prevent="handleSubmit">
        <div class="col-4 c1">
          <div class="form-outline">
            <input type="text" id="form6Example1" class="form-control rounded-pill" v-model="showName" />
            <label class="form-label" for="form6Example1">Show name</label>
          </div>
        </div>

        <div class="col-2 form-outline mb-4 c1">
          <select class="form-select rounded-pill" v-model="rating">
            <option disabled value="">Please select one</option>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </select>
          <label>Rating</label>
        </div>

        <div class=" c2 mx-5">
          <label>Start show on:&nbsp;&nbsp;</label>
          <input type="datetime-local" class="align-self-auto rounded-pill" v-model="startTime" />
        </div>

      <div class="c2">
      <label>End show on:&nbsp;&nbsp;</label>
      <input type="datetime-local" class="align-self-auto rounded-pill" v-model="endTime">
  </div>

<!--      <div class="custom-select">-->
<!--        <div class="select-trigger" @click="toggleDropdown">-->
<!--          <span style="font-size:20px;padding-left: 5px">{{ "fds" }}</span>-->
<!--          <i class="arrow-down"></i>-->
<!--        </div>-->
<!--        <div class="select-options" v-show="isDropdownOpen">-->
<!--          <label v-for="option in options" :key="option.value">-->
<!--            <input type="checkbox" :value="option.value" v-model="selectedValues">-->
<!--            {{ option.label }}-->
<!--          </label>-->
<!--        </div>-->
<!--      </div>-->




      <div class="checkboxes form-check-inline c1">
        <h4 class="border rounded-pill bg-success text-light">Add Tags</h4>
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

      <div class="col-6 form-outline mb-4 c1">
        <input type="number" class="col-4 form-control rounded-pill bg-gradient" v-model="ticketPrice">
        <label>Ticket price</label>
        </div>


      <div class="mb-3">
        <label for="formFile" class="form-label">Default file input example</label>
        <input class="form-control rounded-pill" type="file"  ref="fileInput" accept="image/*" @change="handleFileChange" >
      </div>
      <button type="submit" class="col-2 btn btn-primary c2" >Save</button>


      <!-- Submit button -->
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from "axios";
import NavBar from "@/views/NavBar.vue";
import {useRouter} from "vue-router";
import {useStore} from "vuex";

const state = useStore()
const router = useRouter()
const fileInput = ref(null)
const header = ref('Create a Show')
const showName = ref("")
const rating = ref([])
const startTime = ref("")
const endTime = ref("")
const tags = ref([])
const ticketPrice = ref(0)
const id = ref(router.currentRoute.value.params.Venue)


//handle image upload
const handleFileChange=(event)=>{
  fileInput.value = event.target.files[0]
}

//handle submit
const handleSubmit=()=>{
  const show = {
    showName,
    rating,
    startTime,
    endTime,
    tags,
    ticketPrice
  }
  const form = new FormData()
  form.append("showName",showName)
  form.append("rating",rating)
  form.append("starTime",startTime)
  form.append("endTime",endTime)
  form.append("tags",tags)
  form.append("ticketPrice",ticketPrice)
  form.append("image",fileInput)
  axios.post('http:localhost:8000/admin/'+id.value+'/CreateShow', form,{

    headers:{
      Authorization:`Bearer ${state.state.user.accessToken}`,
      "Content-Type":"multipart/form-data",
    }
  }).then(res=>console.log(res.data)).catch(error=>console.log(error))
}
</script>


<style scoped>

.outer{
  display: flex;
  justify-content: space-around;
}
.left {
  translate: -250px 0px;
}
.checkboxes {
  text-align:center;
}
.custom{
  display: grid;
  place-items: center;
  gap: 20px;
  width: 700px;
}
.c1{
  width: 70%;
}
.c2{
  width: 40%;
  align-self: center;
}


.checkboxes input{
  margin: 0px 20px 0px 0px;
}

.checkboxes label{
  margin: 0px 20px 0px 3px;
}
.custom-select {
  position: relative;
  display: inline-block;
  min-width: 60%;
}

.select-trigger {
  display: flex;
  justify-content: space-between;
  cursor: pointer;
  padding: 3px;
  border: 1px solid #ccc;
  background-color: #fff;

}

.select-options {
  position: absolute;
  top: 100%;
  left: 0;
  display: none;
  padding: 10px;
  background-color: #fff;
  border: 1px solid #ccc;
}

.select-options label {
  display: block;
  margin-bottom: 5px;
}

.arrow-down {
  display: inline-block;
  width: 0;
  height: 0;
  margin-top: 10px;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 5px solid #333;
}

.custom-select.open .select-options {
  display: block;
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