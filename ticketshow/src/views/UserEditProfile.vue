<template>
  <UserLoggedNavBar/>

  <div v-if="err" class="alert alert-danger " role="alert">
    {{ err }}
  </div>
  <div v-if="successmessage" class="alert alert-success " role="alert">
    {{ successmessage }}
  </div>

  <form @submit.prevent="HandleSubmit">
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
            class="m-2 form-control rounded-pill"
            style=""
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
  <UserBottomNavBar/>
</template>

<script setup>

import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
import {computed, onBeforeMount,reactive,watch, ref} from "vue";
import axios from "@/axios";
import router from "@/router";

const image = ref(null)
const successmessage = ref(null)
const err = ref(null)
const details = reactive({
  username:"",
  useremail:""
})
watch([details], ()=>err.value=null)

const handleFileChange = (event) => {
  image.value = event.target.files[0]

}
const HandleSubmit = () => {

  if (image.value) {
    const form = new FormData()
    form.append("username", details.username)
    form.append("email", details.email)
    form.append("image", image.value, image.value.filename)
    const headers = {
      'Content-Type': 'multipart/form-data'
    }


        axios.post("/user/updateprofile", form, {
        headers: headers
      }).then(res => {
        const { message, ...payload } = res.data
          successmessage.value = "User profile updated successfully"
        store.commit("adduser", payload)
        router.push('/user/dashboard')
      }).catch(error => {
        console.log(error)
        err.value = "Error in registering the user."
      })
    }
    else {

      axios.post("/user/updateprofile", { "username": details.username, email: details.email }).then(res => {
        const { message, ...payload } = res.data
        successmessage.value = "User profile update success"
        store.commit("adduser", payload)
        router.push('/user/dashboard')
      }).catch(error => {
        console.log(error)
        err.value = "Error in registering the user."

      })
  }
}



</script>