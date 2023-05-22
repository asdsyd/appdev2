<script setup>
import { reactive } from "vue";
// import {flushPromises} from "@vue/test-utils";
import axios from "axios";
// import * as url from "url";

const details = reactive({
  username: "",
  password: "",
});
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
  axios.post("http://127.0.0.1:8000/user/login", details).then(res => console.log(res.data)).catch(error => console.log(error))
};
</script>
<template>
  <form @submit.prevent="HandleSubmit()">
    <input type="text" v-model="details.username" placeholder="Username" />
    <input type="password" v-model="details.password" placeholder="Password" />
    <input type="submit" value="Submit" placeholder="Submit" />
   <p>new to ticketshow? </p> <router-link :to="'/user/register'">register </router-link>
  </form>
</template>
