<template>
  <user-nav-bar />
  <div class="d-flex justify-content-around">
    <div class="w-50 p-1">
      <select class="form-select" v-model="locationpref">
        <option>Hyderabad</option>
        <option>Delhi</option>
        <option>Mumbai</option>
        <option>Chennai</option>
        <option>Kolkata</option>
        <option>Bangalore</option>
      </select>
      <label class="form-label" for="form6Example5">Location</label>
    </div>
    <div class="d-flex">
      <div class="">
        <label>Start time&nbsp;&nbsp;</label>
        <input
          type="time"
          class="align-self-auto rounded-pill mb-3"
          v-model="startTime"
          @change="checkTime"
        />
      </div>
      &nbsp;
      <div class="">
        <label>End time&nbsp;&nbsp;</label>
        <input
          type="time"
          class="align-self-auto rounded-pill"
          v-model="endTime"
          @change="checkTime"
        />
      </div>
    </div>
  </div>
  <p v-if="!IstimeCorrect" class="text-danger">
    {{ "Start time cannot be greater than endtime" }}
  </p>

  <div v-if="all_Venues && !is_loading" class="accordion">
    <div v-for="v in all_Venues" class="mb-2">
      <h2 class="text-start mb-1  mx-1 accordion-item custom">
       <router-link :to="'/'+v.id+'/details'" style="text-decoration:none;">{{v.name}}</router-link> 
      </h2>
      <div class="d-flex flex-row mx-2 my-2 gap-2 overflow-x-scroll custominner">
        <div v-if="v.movies" v-for="c in v.movies">
          <div class="card h-100" style="width: 300px;">
            <img
              v-if="c.image"
              :src="'http://localhost:8000/image/' + c.image"
              class="card-img-top"
              alt="movie_image"
            />
            <img
              v-else
              src="../assets/movie-icon.png"
              class="card-img-top image-width"
              alt="..."
            />
            <div class="card-body">
              <h5 class="card-title">{{ c.movie_name }}</h5>
              <p v-if="c.rating"><b>rating:</b>{{c.rating.toFixed(1)}}</p>
              <p><b>Starts on</b>:- {{FormatTime(c.start,true)}}</p>
              <p class="card-text"><b>description</b>:- {{ c.description }}</p>
              <p><b>tags:-</b> {{c.tags}}</p>
              <router-link
                v-if="c.seats > 0"
                class="btn btn-primary"
                :to="'/user/' + v.id + '/' + c.movie_id + '/' + 'book'"
                >Book</router-link
              >
              <router-link
              v-else-if="Object.keys($store.state.user).length<=0"
              class="btn btn-primary"
              :to="'/user/login'"
              >Book</router-link
            >
              <button v-if="c.seats<=0" class="btn btn-danger" disabled>
                HouseFull
              </button>
            </div>
          </div>
        </div>
      </div>
      </div>
    </div>
<div v-if="all_Venues.length<=0 && !is_loading">no movies avaliable the moment</div>





  <UserBottomNavBar />
</template>
<script setup>
import {  onBeforeMount, ref } from "vue";
import UserNavBar from "@/views/UserNavBar.vue";
import router from "@/router";
import axios from "@/axios";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
import store from "@/store";


const locationpref = ref(null)
const all_Venues = ref(store.state.venues || []);
const is_loading = ref(true);
const startTime = ref(null)
const endTime = ref(null)
watch([location,startTime,endTime],()=>{
  
})
onBeforeMount(() => {
  if (store.state.venues.length > 0) {
    all_Venues.value = store.state.venues;
    is_loading.value = false;
  } else {
    axios
      .post("/user/getVenues")
      .then((res) => {
        const { venues } = res.data;
        store.commit("addvenues", venues);
        all_Venues.value = store.state.venues;
console.log(all_Venues.value)
        is_loading.value = false;
      })
      .catch((err) => console.log(err));
  }
  console.log(all_Venues.value);
});

const IstimeCorrect = ref(true);

const checkTime = () => {
  
  IstimeCorrect.value = startTime.value < endTime.value;
};
const FormatTime = (time,isend) => {
  const timearr = time.split(" ");
  timearr.shift();
  timearr.pop();
  let timestr
  if(isend){
     timestr = `${timearr[0]}th ${timearr[1]
    }`;
  }
  const Hour =HourFomatterObj[timearr[3].slice(0,2)]
  const Time = timearr[3].slice(3,5)

    timestr = timestr + ` ${Hour[0]}:${Time} ${Hour[1]}`



  return timestr;
  // 2023-05-30T22:29
};
const HourFomatterObj = {
  "00":["12","AM"],
  "01":["1","AM"],
  "02":["2","AM"],
  "03":["3","AM"],
  "04":["4","AM"],
  "05":["5","AM"],
  "06":["6","AM"],
  "07":["7","AM"],
  "08":["8","AM"],
  "09":["9","AM"],
  "10":["10","AM"],
  "11":["11","AM"],
  "12":["12","NOON"],
  "13":["1","PM"],
  "14":["2","PM"],
  "15":["3","PM"],
  "16":["4","PM"],
  "17":["5","PM"],
  "18":["6","PM"],
  "19":["7","PM"],
  "20":["8","PM"],
  "21":["9","PM"],
  "22":["10","PM"],
  "23":["11","PM"],
}

const logout = () => {
  store.commit("removeuser");
  router.push("/user/login");
};
</script>
<style scoped>

.custom{
  width: 99%;
}
.custominner{
  width: 99%;
}
.card-width{
  width: 130%;
}
</style>
