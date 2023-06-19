<template>
  <UserLoggedNavBar/>
  
<div class="d-flex  justify-content-center" v-if="!is_loading">
  <div class="card" style="width: 18rem;">
    <img v-if="!image_present" src="../assets/defaultDP.png" class="card-img-top" alt="...">
    <img v-else :src="image_present" class="text-center card-img-top">
    <div class="card-body">
      <h4 class="card-title">{{username}}</h4>
      <h4 class="card-title">{{useremail}}</h4>
    </div>
  </div>

  <div>
    <p>
      Click <router-link to="changePassword" >here  </router-link>to change password
    </p>
  </div>
  </div>



  <UserBottomNavBar/>
</template>
<script setup>
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
import {computed, onBeforeMount, ref} from "vue";
import axios from "@/axios";
const is_loading = ref(true)
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
      image_present.value = `http://localhost:8000/profile_image/${image}`
      is_loading.value = false
    } else{
      const [name,email] = res.data
      username.value = name
      useremail.value=email
      is_loading.value = false
    }

  }).catch(err=>console.log(err))
})


</script>