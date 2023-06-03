<script setup>
import { reactive, ref } from "vue";
import { useStore } from "vuex";
import axios from "../axios";
import { computed } from "vue";
import { useRouter } from "vue-router";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
// import * as url from "url";
const image = ref(null)
const err = ref(null)
const store = useStore()
const router = useRouter()
const details = reactive({
  username: "",
  password: "",
  retypepassword: "",
  email: "",
});
const passwordMatch = computed(() => details.password === details.retypepassword)

const handleFileChange = (event) => {
  image.value = event.target.files[0]

}
const HandleSubmit = () => {

  if (image.value) {
    const form = new FormData()
    form.append("username", details.username)
    form.append("password", details.password)
    form.append("email", details.email)
    form.append("image", image.value, image.value.filename)
    const headers = {
      'Content-Type': 'multipart/form-data'
    }

    axios.post("/user/register", form, {
      headers: headers
    }).then(res => {
      const { message, ...payload } = res.data
      store.commit("adduser", payload)
      router.push('/user/dashboard')
    }).catch(error => {
      console.log(error)
      if (error.response.data) {
        err.value = error.response.data.message
      }
    })
  }
  else {

    axios.post("/user/register", { "username": details.username, password: details.password, email: details.email }).then(res => {
      const { message, ...payload } = res.data
      store.commit("adduser", payload)
      router.push('/user/dashboard')
    }).catch(error => {
      console.log(error)
      if (error.response.data) {
        err.value = error.response.data.message
      }
    })
  }


};

// const handleClick = (e) => {
//     const [name,value] = e.target
//     details[name] = value
// };
// const secondR = reactive({
//     access:"",
//     refreshToken:"",
//     username:"",
// })
</script>
<template>
  <div v-if="err" class="alert alert-danger " role="alert">
    {{ err }}
  </div>
  <form @submit.prevent="HandleSubmit()">
    <div>
      <h1 class="form-label container mt-4">Welcome to TicketShow! Please register to book tickets.</h1>
    </div>
    <div class="mt-4 mb-3 col-3 container">
      <input class="container col-3 form-control rounded-pill " type="text" v-model="details.username"
        placeholder="Username" />
    </div>
    <div class="mt-4 mb-3 col-3 container">
      <input class="container col-3 form-control rounded-pill " type="password" v-model="details.password"
        placeholder="Password" />
    </div>
    <div class="mt-4 mb-3 col-3 container">
      <input class="container col-3 form-control rounded-pill " type="password" v-model="details.retypepassword"
        placeholder="Re-type password" />
    </div>
    <div class="mt-4 mb-3 col-3 container">
      <input class="container col-3 form-control rounded-pill " type="email" v-model="details.email"
        placeholder="Email" />
    </div>
    <div class="mt-4 mb-3 col-3 container">

      <input class="form-control rounded-pill" type="file" accept="image/*" @change="handleFileChange">
      <label for="formFile" class="form-label ">Choose a profile image</label>
    </div>
    <div class="mt-4 mb-3 col-3 container">
      <input class="container mb-3 px-4 btn btn-outline-primary rounded-pill" type="submit" value="Register"
        placeholder="Register" :disabled='!passwordMatch' />
    </div>

    <h6 class="text-success-emphasis">Already have an account? </h6> <router-link class="text-decoration-none"
      :to="'/user/login'">login </router-link>
</form>

<UserBottomNavBar /></template>
