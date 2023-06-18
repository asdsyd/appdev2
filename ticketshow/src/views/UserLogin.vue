<script setup>
import { useStore } from "vuex";
import { reactive,ref ,watch} from "vue";
import axios from "../axios";
import { useRouter } from "vue-router";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";


const details = reactive({
  username: "",
  password: "",
});
const store = useStore()
const err = ref(null)
const router = useRouter()
watch(details,()=>err.value=null)
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
  }).catch(error =>{
    if(error.response){
      if(error.response.data){
        err.value = error.response.data.message
      }
    }
  })
};
</script>
<template>
  <form @submit.prevent="HandleSubmit()">
    <div>
      <h1 class="form-label container mt-4">Welcome back! Please login to continue...</h1>
    </div>
    <div v-if="err" class="alert alert-danger " role="alert">
      {{ err }}
    </div>
    <div class="mt-4 mb-3 col-3 container ">
    <input class="container col-3 form-control rounded-pill " type="text" v-model="details.username" placeholder="Username" />
    </div>
    <div class="mt-3 mb-3 col-3 container">
    <input class="container col-3 form-control rounded-pill" type="password" v-model="details.password" placeholder="Password" />
    </div>
    <div class="mt-3 col-3 container">
    <input class="container mb-3 px-4 btn btn-outline-primary rounded-pill" type="submit" value="Login" placeholder="Login" />
    </div>
   <h6 class="text">New to ticketshow? </h6> <router-link :to="'/user/register'" class="link-offset-1-hover text-decoration-none">register </router-link>

  </form>

  <UserBottomNavBar/>
</template>
