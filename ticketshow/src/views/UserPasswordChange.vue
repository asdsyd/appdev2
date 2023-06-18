<template>
  <user-nav-bar/>
  <div v-if="err" class="alert alert-danger " role="alert">
    {{ err }}
  </div>
  <div v-if="successmessage" class="alert alert-success " role="alert">
    {{ successmessage }}
  </div>
  <form @submit.prevent="handlepasschange">
  <div class="container mt-4">
    <div>
    <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" type="password" v-model="details.oldpassword"
           placeholder="Old Password">

    </div>
    <div>
    <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" type="password" v-model="details.password"
           placeholder="New Password">

    </div>
    <div>
    <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" type="password" v-model="details.retypepassword"
           placeholder="Confirm New Password">

    </div>
    <button class="btn btn-warning rounded-pill col-3 m-2" type="submit" value="Change Password" :disabled="!passwordMatch" submit.prevent>Change Password</button>
  </div>
</form>
</template>
<script setup>
import UserNavBar from "@/views/UserNavBar.vue";
import {computed, reactive,ref,watch} from "vue";
import axios from "@/axios"
import router from "@/router";

const successmessage = ref(null)
const err = ref(null)
const passwordMatch = computed(() => details.password === details.retypepassword)
const details = reactive({
  oldpassword: "",
  password: "",
  retypepassword: "",
});
watch([details],()=>err.value=null)

const handlepasschange = ()=>{
 axios.post('/user/passchange',{oldpassword:details.oldpassword,password:details.password}).then(res=>{successmessage.value = res.data.message
setTimeout(()=>router.push('/user/dashboard'),1000)
}).catch(error=>err.value="error in changing password" )
}
</script>