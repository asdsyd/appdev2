<script setup>
import { useStore } from "vuex";
import { reactive } from "vue";
import axios from "../axios";
import { useRouter } from "vue-router";


const details = reactive({
  username: "",
  password: "",
});
const store = useStore()
const router = useRouter()
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
  axios.post("/user/login", details).then(res => {
    const {message,...rest} = res.data
    store.commit('adduser',rest)
    router.push('/user/dashboard')
  }).catch(error => console.log(error))
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
