
<template>
  <NavBar></NavBar>
  <div class=" container show-pill" >
    <h1 class="px-5 text-light display-4 rounded-pill show-pill-inside cust">{{ header }}</h1>
  </div>
  <div class="outer">
    <!--    creating create-show form-->
    <form class="m-3 custom" @submit.prevent="handleSubmit" >
        <div class="col-4 c1">
          <div class="form-outline">
            <input type="text" id="form6Example1" class="form-control rounded-pill" v-model="showName" />
            <label class="form-label" for="form6Example1">Show name</label>
          </div>
        </div>

<div>
        <div class="">
          <label>Start show on:&nbsp;&nbsp;</label>
          <input type="datetime-local" class="align-self-auto rounded-pill" v-model="startTime" @change="checkTime" />
        </div>

      <div class="">
      <label>End show on:&nbsp;&nbsp;</label>
      <input type="datetime-local" class="align-self-auto rounded-pill" v-model="endTime" @change="checkTime">
      </div>
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



      <h3 v-if="!IstimeCorrect" class="text-danger">{{"Start time cannot be greater than endtime"}}</h3>
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

      <div class="col-6 form-outline mb-4 ">
        <input type="number" class="col-4 form-control rounded-pill bg-gradient" v-model="ticketPrice" >
        <label>Ticket price</label>
        </div>


      <div class="mb-3 c1">
        <label for="formFile" class="form-label ">Choose the Show's Image</label>
        <input class="form-control rounded-pill" type="file"  accept="image/*" @change="handleFileChange" >
        <button type="submit" class="col-2 btn btn-primary c2 c4" >Save</button>
        <h1 v-if="err" class="text-danger-emphasis">{{err}}</h1>
      </div>




      <!-- Submit button -->
    </form>
  </div>
</template>

<script setup>
import {computed, ref} from 'vue'
import Newinstance from "axios";
import NavBar from "@/views/NavBar.vue";
import {useRouter} from "vue-router";
import {useStore} from "vuex";
import store from '@/store';

const state = useStore()
const router = useRouter()
const fileInput = ref(null)
const header = ref('Create a Show')
const showName = ref("")
const startTime = ref("")
const endTime = ref("")
const tags = ref([])
const ticketPrice = ref()
const id = ref(router.currentRoute.value.params.Venue)
const err = ref(null)
const IstimeCorrect= ref(true)

//handle image upload
const handleFileChange=(event)=>{
  fileInput.value = event.target.files[0]

}
const checkTime = ()=>{
  IstimeCorrect.value= startTime.value<endTime.value
}

//handle submit
const handleSubmit=()=>{
  const form = new FormData()
console.log(tags.value)
  form.append("showName",showName.value)
  form.append("startTime",startTime.value)
  form.append("endTime",endTime.value)
  form.append("tags",tags.value)
  form.append("ticketPrice",ticketPrice.value)
  if(fileInput.value){
    form.append("image",fileInput.value,fileInput.value.name)
  }

  const contype = fileInput.value?'multipart/form-data':"application/json"
 const headers = {


// Set the desired headers
  'Authorization': `Bearer ${state.state.user.accessToken}`,
  'Content-Type': contype
 }


  Newinstance.post('http://localhost:8000/admin/'+ id.value+ '/CreateShow',form,{

    headers:headers


  }).then(res=>router.push('/admin/'+store.state.user.username)).catch(error=>{
    if(error.response){
      if(error.response.status=401){
        err.value = error.response.data.message
      }
    }

    console.log(error)
  })
}
</script>

<style scoped>

.cust{
  margin-top:3%;
}
label{
  font-weight: bolder;
}
.outer{
  display: flex;
  justify-content: center;
}
.left {
  translate: -250px 0px;
}
.checkboxes {
  text-align:center;
}

.custom{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  flex-direction: column;
  gap: 20px;
  min-height: fit-content;
  width: 900px;
}
.c1{
  width: 50%;
}
.c2{
  width: 25%;
}
.c3{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.c4{
  margin-top:20px;
}
@media screen and (max-width:722px) {
  .custom{
    display: flex;
    flex-flow:column nowrap;
    align-items: center;
    gap: 20px;
    min-height: fit-content;
  }
  .c1{
    width:50%
  }
  .c2{
  width:30%
      }
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