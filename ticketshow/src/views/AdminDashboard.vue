<template>
  <NavBar></NavBar>

  <div v-if="venues"  v-for="v in venues" class="m-lg-3 card mb-3 border-primary" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Venue_01</h5>
      <p class="card-text">No shows created</p>
      <div>
        <button class=" m-3 rounded-circle btn btn-primary">+</button>
      </div>
      <button class="btn btn-success">Edit</button>
      <button href="#" class="btn btn-danger">Delete</button>
    </div>
  </div>

  <div class="m-lg-3 card mb-3 border-dotted " style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title text-bg-light">New Venue</h5>
      <p class="card-text">Click on the buttion below to add Venue</p>
      <div>
        <button class=" m-3 rounded-circle btn btn-success">r+</button>
      </div>
    </div>
  </div>

  <div v-show="expire"  style="display:block;" class="modal" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title"></h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true" @click="()=>expire.value=false">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p>Your Session has Expired</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="refresh"></button>
          <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="logout">cancel</button>
        </div>
      </div>
    </div>
  </div>

</template>
<script setup>
import {ref} from "vue";
import NavBar from "@/views/NavBar.vue";
import { useStore } from 'vuex';
import axios from '../axios';
import router from "@/router";


const expire = ref(false)
const store = useStore()
const venues = store.state.venues
axios.get('/admin/getVenues').then(res=>{
  const venues = res.data.venues
  store.commit("addvenues",venues)
}).catch(e=>{
  console.log(e.response.data)
  if(e.response.data.msg==="Token has Expired"){
expire.value= true
  }
   else{
     router.push('/admin/login')
}

})
const refresh =()=>{
 axios.post('/admin/refresh',{
   headers:{
     Authorization:`Bearer ${$store.state.user.refresh_token}`
   }
 }).then(res=>{

 })
}

const logout = ()=>{
  store.commit('removeuser')
  router.push('/admin/login')
}
</script>