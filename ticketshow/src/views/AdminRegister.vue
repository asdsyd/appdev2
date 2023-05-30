<script setup>
import { reactive } from "vue";
import {useStore} from "vuex";

import axios from "../axios";
import {computed} from "vue";
import {useRouter} from "vue-router";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
// import * as url from "url";


const store = useStore()
const router = useRouter()
const details = reactive({
  username: "",
  password: "",
  retypepassword: "",
  email: "",
});
const passwordMatch = computed(()=> details.password===details.retypepassword)
// const handleClick = (e) => {
//     const [name,value] = e.target
//     details[name] = value
// };
// const secondR = reactive({
//     access:"",
//     refreshToken:"",
//     username:"",
// })
const HandleSubmit = () => {
  const actualDetails = {username:details.username, password:details.password, email:details.email}
  axios.post("/user/register", actualDetails).then(res => {
    const {message,...payload}=  res.data
    store.commit("adduser",payload)
    router.push('/user/dashboard')
  }).catch(error => console.log(error))
};
</script>
<template>
  <form @submit.prevent="HandleSubmit()">
    <div>
      <h1 class="form-label container mt-4">Admin Register</h1>
    </div>
    <div class="alert alert-warning" role="alert">
      Only for authorised Super Admin. If you are an admin, <span> <router-link class="link-success" to="'/admin/login'"> click here to login </router-link> </span>
    </div>
    <div v-if="err" class="alert alert-danger " role="alert">
      {{ err }}
    </div>
    <div class="mt-4 mb-3 col-3 container ">
      <input class="container col-3 form-control rounded-pill " type="text" v-model="details.username" placeholder="Admin Username" />
    </div>
    <div class="mt-3 mb-3 col-3 container">
      <input class="container col-3 form-control rounded-pill" type="password" v-model="details.password" placeholder="Admin Password" />
    </div>
    <div class="mt-3 mb-3 col-3 container">
      <input class="container col-3 form-control rounded-pill" type="password" v-model="details.retypepassword" placeholder="Re-enter Admin Password" />
    </div>
    <div class="mt-3 mb-3 col-3 container">
      <input class="container col-3 form-control rounded-pill" type="email" v-model="details.email" placeholder="Admin Email" />
    </div>
    <div class="mt-3 col-3 container">
      <input class="container mb-3 px-4 btn btn-outline-primary rounded-pill" type="submit" value="Register Admin" :disabled='!passwordMatch' />
    </div>
  </form>

  <user-bottom-nav-bar/>
<!--    <form @submit.prevent="HandleSubmit()">-->
<!--    <input type="text" v-model="details.username" placeholder="Username" />-->
<!--    <input type="password" v-model="details.password" placeholder="Password" />-->
<!--    <input type="password" v-model="details.retypepassword" placeholder="Re-type password" />-->
<!--    <input type="email" v-model="details.email" placeholder="Email" />-->
<!--    <input type="submit" value="Submit" placeholder="Submit" :disabled='!passwordMatch'/>-->
<!--    <p>already have an account?  </p> <router-link :to="'/user/login'">login </router-link>-->
<!--  </form>-->
</template>
