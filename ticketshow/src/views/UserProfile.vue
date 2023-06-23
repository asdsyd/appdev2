<template>
  <UserLoggedNavBar/>
  
<div class="d-flex  justify-content-center container " v-if="!is_loading">
  <div class="card w-40" style="width: 18rem;">
    <div class="card-header">Your Profile</div>
    <img v-if="!image_present" src="../assets/defaultDP.png" class="card-img-top" alt="...">
    <img v-else :src="image_present" class="text-center card-img-top">
    <div class="card-body p-2">
      <h6 class="card-title d-flex justify-content-start"><span class="text-info"> Username: </span> {{username}}</h6>
      <h6 class="card-title d-flex justify-content-start"><span class="text-info">Email: </span> {{useremail}}</h6>
    </div>

    <div>
      <p>
        Click <router-link to="updateProfile" >here  </router-link>to update your profile
      </p>
    </div>
    <div>
    <p>
      Click <router-link to="changePassword" >here  </router-link>to update your password
    </p>
    </div>
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