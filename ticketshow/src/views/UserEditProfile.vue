<template>
  <UserLoggedNavBar/>

  <div v-if="err" class="alert alert-danger " role="alert">
    {{ err }}
  </div>
  <div v-if="successmessage" class="alert alert-success " role="alert">
    {{ successmessage }}
  </div>

  <form @submit.prevent="handleupdateprofile">
    <div class="container mt-4">
      <div>
        <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" type="text" v-model="details.username"
               placeholder="New Username">

      </div>
      <div>
        <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" type="email" v-model="details.email"
               placeholder="New Email">
      </div>

      <div class="">
        <label for="formFile" >Choose new profile image</label>
      </div>
      <div>
        <input
            class="m-2 form-control rounded-pill w-50 "
            style="width: 50%"
            type="file"
            accept="image/*"
            @change="handleFileChange"
        />

      </div>
      <div>
        <button type="submit" class="rounded-pill  m-2 py-1 border-warning-subtle btn-warning btn">Update Profile</button>
        <h1 v-if="err" class="text-danger-emphasis">{{ err }}</h1>

      </div>

    </div>
  </form>

  <div class="d-flex  justify-content-center container " v-if="!is_loading">
    <div class="card w-40" style="width: 18rem;">
      <div class="card-header">Profile Preview</div>
      <img v-if="!image_present" src="../assets/defaultDP.png" class="card-img-top" alt="...">
      <img v-else :src="image_present" class="text-center card-img-top">
      <div class="card-body p-2">
        <h6 class="card-title d-flex justify-content-start"><span class="text-info"> Username: </span> {{username}}</h6>
        <h6 class="card-title d-flex justify-content-start"><span class="text-info">Email: </span> {{useremail}}</h6>
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
import {computed, onBeforeMount,reactive,watch, ref} from "vue";
import axios from "@/axios";
import router from "@/router";

const successmessage = ref(null)
const err = ref(null)
const details = reactive({
  oldusername: "",
  username: "",
  oldemail: "",
  email: "",
})
watch([details], ()=>err.value=null)
const handleupdateprofile = () => {
  axios.post('/user/updateprofile', {oldusername:details.oldusername,username:details.username,oldemail:details.oldemail,email:details.email}).then(res=>{successmessage.value = res.data.message
setTimeout(()=>router.push(':username/profile'), 1000)  }).catch(error=>err.value="error in updating profile")
}

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