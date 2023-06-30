<template>
  <NavBar></NavBar>
  <div v-if="isloading" class="text-center">
      <div class="spinner-border" role="status">
        <span class="sr-only"></span>
      </div>
    </div>
  <div class=" custom mx-5 my-3 d-flex flex-row flex-wrap ">
    <div
      v-if="venue_checker && !isloading"
      v-for="v in all_venues.venues"
      class="m-3 p-2 card  border-warning-subtle custominner"
  style="width: 300px; background-image: linear-gradient(sandybrown, mediumpurple)"
    >
      <div class="card-body">
        <h5 class="card-title text-light">{{ v.name }}</h5>
        <p v-if="!v.movies?.length > 0" class="card-text">No shows created</p>
        <div>
          <div
            v-for="c in v.movies"
            class=" card mb-2 border-primary-subtle "
            style="background-image: linear-gradient(honeydew, gainsboro)"
          >
            <div class="card-body">
              <h5 class="card-title">{{ c.movie_name }}</h5>
              <router-link
                class="m-2 btn btn-outline-primary rounded-5 text-decoration-none"
                :to="'/admin/'+ v.id+'/'+ c.movie_id + '/EditShow'"
                >Edit</router-link
              >
              <button
                class="m-2 btn btn-outline-danger rounded-5 text-decoration-none"
                @click="handleShowdelete({venue:v.id,show:c.movie_id})"
              >
                Delete
              </button>
            </div>
          </div>
          <router-link
            class="m-3 rounded-pill btn btn-primary"
            :to="'/admin/' + v.id + '/CreateShow'"
            >+ add movie</router-link
          >
        </div>
        <router-link
          class="m-2 btn btn-warning rounded-5 text-decoration-none"
          :to="'/admin/' + v.id + '/EditVenue'"
          >Edit</router-link
        >
        <button
          class="m-2 btn btn-danger rounded-5 text-decoration-none"
          @click="DeleteModal(v.id)"
        >
          Delete
        </button>
      </div>
      <button class="rounded-pill" :disabled="(Object.keys($store.state.export_id).length>0)" @click="sendexporttask(v.id)">
        export csv
      </button>
    </div>
    <!--    nested cards have to be fixed heres the help link https://stackoverflow.com/questions/67667887/nested-cards-fitting-cards-within-a-card-bootstrap-cards-->

    <div v-if="!isloading" class="m-3 p-2  card " style="width: 300px;
border-style: dashed; border-color: black">
      <div class="card-body">
        <h5 class="card-title text-bg-light" >New Venue</h5>
        <p class="text-wrap mt-3">Click on the button below to create a Venue</p>
        <div>
          <router-link
            class="m-2 btn btn-outline-success rounded-5 text-decoration-none"
            to="/admin/CreateVenue"
            >+</router-link
          >
        </div>
      </div>
    </div>
  </div>

  <div
    v-show="expire"
    style="display: block"
    class="modal"
    tabindex="-1"
    role="dialog"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Login Expired</h5>
        </div>
        <div class="modal-body">
          <p>Your Session has Expired</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="refresh">
            refresh
          </button>
          <button
            type="button"
            class="btn btn-secondary"
            data-dismiss="modal"
            @click="Adminlogout"
          >
            cancel
          </button>
        </div>
      </div>
    </div>
  </div>





  <div
    v-show="deleter"
    style="display: block"
    class="modal"
    tabindex="-1"
    role="dialog"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Delete Confirmation</h5>
        </div>
        <div class="modal-body">
          <p>Do you really want to delete this Venue?</p>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-danger"
            @click="handledelete(venue_to_delete_id)"
          >
            Yes
          </button>
          <button
            type="button"
            class="btn btn-primary"
            data-dismiss="modal"
            @click="cancelDelete('venue')"
          >
            No
          </button>
        </div>
      </div>
    </div>
  </div>



  <div
    v-show="Showdeleter"
    style="display: block"
    class="modal"
    tabindex="-1"
    role="dialog"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Delete Confirmation</h5>
        </div>
        <div class="modal-body">
          <p>Do you really want to delete this Show?</p>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-danger"
            @click="deleteShow(Show_to_delete)"
          >
            Yes
          </button>
          <button
            type="button"
            class="btn btn-primary"
            data-dismiss="modal"
            @click="cancelDelete('show')"
          >
            No
          </button>
        </div>
      </div>
    </div>
  </div>

  <user-bottom-nav-bar/>
</template>
<script setup>
import { computed, reactive, ref, watch } from "vue";
import NavBar from "@/views/NavBar.vue";
import { useStore } from "vuex";
import axios from "../adminaxios";
import NewAxios from "axios";
import { useRouter } from "vue-router";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";

const isloading = ref(true)
const deleter = ref(false);
const Showdeleter= ref(false)
const Show_to_delete=reactive({
  venue:null,
  show:null
})
const venue_to_delete_id = ref(null);
const router = useRouter();
const expire = ref(false);
const store = useStore();
let all_venues = reactive({
  venues: store.state.venues,
});


const sendexporttask = (id)=>{
axios.get('/admin/export/' + id).then(res=>{
  const obj  = {
    task:id,
    task_id:res.data.id 
  }
  store.commit("addtask",obj)
  window.location.reload()
}).catch(e=>{
  alert("exporting error")
})
}

const handleShowdelete=(id)=>{
  console.log(id)
  Showdeleter.value=true
  Show_to_delete.venue = id.venue
  Show_to_delete.show= id.show
}

const deleteShow = (obj)=>{
  console.log(obj)
  axios.delete('/admin/'+ obj.venue + '/' + obj.show +'/deleteShow' ).then(res=>{
    window.location.reload()
  }).catch(e=>{
    console.log(e)
  })
}

const cancelDelete = (which) => {
  if(which==="show"){
   Showdeleter.value=false
   Show_to_delete.venue=null
    Show_to_delete.show=null
}else{
  deleter.value = false;
  venue_to_delete_id.value = null;
}
};
const DeleteModal = (id) => {
  deleter.value = true;
  venue_to_delete_id.value = id;
};
const venue_checker = computed(() => {
  return all_venues.venues.length > 0;
});

axios
  .get("/admin/getVenues")
  .then((res) => {
    const venues = res.data.venues;
console.log(venues)
    store.commit("addvenues", venues);
    all_venues.venues = store.state.venues;
    isloading.value=false
  })
  .catch((e) => {
    if(e.response){
    if (e.response.data.msg === "Token has expired") {
      expire.value = true;
    } else {
      router.push("/admin/login");
    }
  }else{
    store.commit("removeadmin")
    router.push('/admin/login')
  }
  });
const refresh = () => {
  NewAxios.post("http://localhost:8000/admin/refresh", null, {
    headers: {
      Authorization: `Bearer ${store.state.admin.refresh_token}`,
    },
  })
    .then((res) => {
      const { message, ...rest } = res.data;
      store.commit("refresheradmin", rest);
      expire.value = false;
    })
    .catch((e) => {
      store.commit("removeadmin");
      router.push({ path: "/admin/login" });
    });
};
const handledelete = (id) => {
  store.commit("deleteVenue", id);
  axios
    .delete("/admin/" + id + "/deleteVenue")
    .then((res) => {
      deleter.value = false;
      window.location.reload();
    })
    .catch((er) => {
      console.log(er);
    });
};

const Adminlogout = () => {
  store.commit("removeadmin");
  router.push("/admin/login");
};
</script>
<style scoped>
.custom{
  border: transparent;
}
@media screen and (max-width:737px) {
  .custom{
flex-direction: column;
margin: 5px;
 }
  .custominner{
margin-bottom: 10px;
  }
}

</style>
