<script setup>
import { reactive } from "vue";
import {useStore} from "vuex";

import axios from "axios";
import {computed} from "vue";
import {useRouter} from "vue-router";
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
  axios.post("http://127.0.0.1:8000/user/register", actualDetails).then(res => {
    const {message,...payload}=  res.data
    store.commit("adduser",payload)
  }).catch(error => console.log(error))
};
</script>
<template>
  <form @submit.prevent="HandleSubmit()">
    <input type="text" v-model="details.username" placeholder="Username" />
    <input type="password" v-model="details.password" placeholder="Password" />
    <input type="password" v-model="details.retypepassword" placeholder="Re-type password" />
    <input type="email" v-model="details.email" placeholder="Email" />
    <input type="submit" value="Submit" placeholder="Submit" :disabled='!passwordMatch'/>
  </form>
</template>
