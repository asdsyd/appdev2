<template>
  <UserLoggedNavBar/>

  <div class="card" style="width: 18rem;">
    <img v-if="!image_present" src="../assets/defaultDP.png" class="card-img-top" alt="...">
    <img v-else :src="image_present" class="text-center card-img-top">
    <div class="card-body">
      <h5 class="card-title">Card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item">An item</li>
      <li class="list-group-item">A second item</li>
      <li class="list-group-item">A third item</li>
    </ul>
    <div class="card-body">
      <a href="#" class="card-link">Card link</a>
      <a href="#" class="card-link">Another link</a>
    </div>
  </div>



  <UserBottomNavBar/>
</template>
<script setup>
import UserNavBar from "@/views/UserNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
import {computed, onBeforeMount, ref} from "vue";
import axios from "@/axios";
const image_present = ref(null)
const image_display = computed(()=>image_present.value!==null)
const username = ref(null)
const useremail = ref(null)
onBeforeMount(()=>{
  axios.get('/user/getuser').then(res=>{
    if(res.data.length>2){
      const [name,email,image] = res.data
username.value = name
      useremail.value = email
    } else{
      const [name.email] = res.data
    }

  }).catch(err=>console.log(err))
})


</script>