<template>
  <NavBar></NavBar>
  <div class="d-flex flex-wrap flex-row">
  <div v-if="venue_checker"  v-for="v in all_venues.venues" class="m-lg-3 card mb-3 border-primary" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">{{v.name}}</h5>
      <p v-if="!v.movies?.length>0" class="card-text">No shows created</p>
      <div>
        <div v-for="c in v.movies" class="m-lg-3 card mb-3 border-primary" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">{{c.movie_name}}</h5>
            <router-link class="m-2 btn btn-outline-primary rounded-5 text-decoration-none" :to="'/admin/' + c.movie_id + '/EditShow'">Edit</router-link>
            <button  class="m-2 btn btn-outline-danger rounded-5 text-decoration-none" @click="handleShowdelete(c.id)">Delete</button>
          </div>
        </div>
        <router-link class=" m-3 rounded-circle btn btn-primary" :to="'/admin/' + v.id +'/CreateShow'">+</router-link>
      </div>
      <router-link class="m-2 btn btn-outline-primary rounded-5 text-decoration-none" :to="'/admin/' + v.id + '/EditVenue'">Edit</router-link>
      <button  class="m-2 btn btn-outline-danger rounded-5 text-decoration-none" @click="DeleteModal(v.id)">Delete</button>
    </div>
  </div>
<!--    nested cards have to be fixed heres the help link https://stackoverflow.com/questions/67667887/nested-cards-fitting-cards-within-a-card-bootstrap-cards-->


  <div class="m-lg-3 card mb-3 border-dotted " style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title text-bg-light">New Venue</h5>
      <p class="card-text">Click on the buttion below to add Venue</p>
      <div>
        <router-link class="m-2 btn btn-success rounded-5" to="/admin/CreateVenue">+</router-link>
      </div>
    </div>
  </div>
  </div>

  <div v-show="expire"  style="display:block;" class="modal" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Login Expired</h5>
        </div>
        <div class="modal-body">
          <p>Your Session has Expired</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="refresh">refresh</button>
          <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="logout">cancel</button>
        </div>
      </div>
    </div>
  </div>

  <div v-show="deleter"  style="display:block;" class="modal" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Delete Confirmation</h5>
        </div>
        <div class="modal-body">
          <p>Do you want to delete this Venue</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="handledelete(venue_to_delete_id)">yes</button>
          <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="cancelDelete">no</button>
        </div>
      </div>
    </div>
  </div>

</template>
<script setup>
import {computed, reactive, ref, watch} from "vue";
import NavBar from "@/views/NavBar.vue";
import { useStore } from 'vuex';
import axios from '../axios';
import NewAxios from 'axios';
import {useRouter} from "vue-router";

const deleter = ref(false)
const venue_to_delete_id = ref(null)
const router  = useRouter()
const expire = ref(false)
const store = useStore()
let all_venues= reactive({
  venues:store.state.venues
})

const cancelDelete = ()=>{
  deleter.value = false
  venue_to_delete_id.value=null
}
const DeleteModal = (id)=>{
  deleter.value = true
  venue_to_delete_id.value=id
}
const venue_checker = computed(()=>{
  return all_venues.venues.length>0})


axios.get('/admin/getVenues').then(res=>{
  const venues = res.data.venues


  store.commit("addvenues",venues)
  all_venues.venues= store.state.venues
}).catch(e=>{

  if(e.response.data.msg==="Token has expired"){
expire.value= true

  }
   else{
     router.push('/admin/login')
}

})
const refresh =()=>{
 NewAxios.post('http://localhost:8000/admin/refresh',null, {
   headers: {
   Authorization:`Bearer ${store.state.user.refresh_token}`
 }
 }).then(res=>{
const {message,...rest} = res.data
   store.commit("refresher",rest)
   expire.value=false

 }).catch(e=>{
   store.commit("removeuser")
   router.push({path:'/admin/login'})
 })
}
const handledelete=(id)=>{
  store.commit("deleteVenue",id)
  axios.delete("/admin/"+id+"/deleteVenue").then(res=>{deleter.value=false}).catch(er=>console.log(er))
}

const logout = ()=>{
  store.commit('removeuser')
  router.push('/admin/login')
}
</script>