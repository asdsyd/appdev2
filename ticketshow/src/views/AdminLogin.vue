<script setup>
import {onBeforeMount, reactive, ref,watch} from "vue";

import axios from "../axios";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import UserNavBar from "@/views/UserNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
// import * as url from "url";

const details = reactive({
  username: "",
  password: "",
});


const err = ref(null)
const store = useStore()
const router = useRouter()
watch(details,()=>err.value=null)
onBeforeMount(()=>{

  const store =useStore()

  if(Object.keys(store.state.user).length>0){
    router.push('/admin/'+store.state.admin.username)
  }

})

const HandleSubmit = () => {
  axios.post("/admin/login", details).then(res => {
    const {message,...payload}=  res.data
    store.commit("removeuser")
    store.commit("addadmin",payload)
    setTimeout(() => {router.push(`/admin/${payload.username}`)
    }, 1000);
  }).catch(error =>{
    console.log(error)
    err.value = "error in admin login"
  })

};
</script>
<template>
  <form @submit.prevent="HandleSubmit()">
    <div>
      <h1 class="form-label container mt-4">Admin Login</h1>
    </div>
    <div v-if="err" class="alert alert-danger " role="alert">
      {{ err }}
    </div>
    <div class="mt-4 mb-3 col-5 container ">
      <input class="container col-6 form-control rounded-pill " type="text" v-model="details.username" placeholder="Admin Username" />
    </div>
    <div class="mt-3 mb-3 col-5 container">
      <input class="container col-3 form-control rounded-pill" type="password" v-model="details.password" placeholder="Admin Password" />
    </div>
    <div class="mt-3 col-3 container">
      <input class="container mb-3 px-4 btn btn-outline-primary rounded-pill" type="submit" value="Login" placeholder="Admin Login" />
    </div>

  </form>
  <user-bottom-nav-bar/>
<!--  <form @submit.prevent="HandleSubmit()">-->
<!--    <input type="text" v-model="details.username" placeholder="Username" />-->
<!--    <input type="password" v-model="details.password" placeholder="Password" />-->
<!--    <input type="submit" value="Submit" placeholder="Submit" />-->
<!--  </form>-->
</template>
