<script setup>
import { reactive } from "vue";
// import {flushPromises} from "@vue/test-utils";
import axios from "../axios";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
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
const store = useStore()
const router = useRouter()
const HandleSubmit = () => {
  axios.post("/admin/login", details).then(res => {
    const {message,...payload}=  res.data
    store.commit("adduser",payload)
    router.push(`/admin/${payload.username}`)
  }).catch(error => console.log(error))

};
</script>
<template>
  <form @submit.prevent="HandleSubmit()">
    <input type="text" v-model="details.username" placeholder="Username" />
    <input type="password" v-model="details.password" placeholder="Password" />
    <input type="submit" value="Submit" placeholder="Submit" />
  </form>
</template>
