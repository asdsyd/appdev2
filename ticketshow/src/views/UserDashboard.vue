<template>
  <user-nav-bar />
  <div v-if="all_Venues && !is_loading" class="accordion">
    <div v-for="v in all_Venues" class="mb-2" >
      <h2 class="text-start mb-1  mx-1 accordion-item custom">
       <router-link :to="'/'+v.id+'/details'" style="text-decoration:none;">{{v.name}}</router-link> 
      </h2>
      <div class="container d-flex flex-row mx-2 my-2 overflow-x-scroll">
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
                :to="'/admin/' + v.id + '/' + c.movie_id + '/' + 'book'"
                >Book</router-link
              >
              <button v-else class="btn btn-danger" disabled>
                HouseFull
              </button>
            </div>
          </div>
        </div>
      </div>
      </div>
    </div>
<div v-if="all_Venues.length<=0 && !is_loading">no movies avaliable the moment</div>



  <!--  <div class="row row-cols-1 row-cols-md-3 g-4 container">-->
  <!--    <div class="col">-->
  <!--      <div class="card h-100">-->
  <!--        <img src="../assets/movie-icon.png" class="card-img-top" alt="...">-->
  <!--        <div class="card-body">-->
  <!--          <h5 class="card-title">Card title</h5>-->
  <!--          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>-->
  <!--          <a href="#" class="btn btn-primary">Book</a>-->
  <!--        </div>-->
  <!--      </div>-->
  <!--    </div>-->
  <!--    <div class="col">-->
  <!--      <div class="card h-100">-->
  <!--        <img src="../assets/movie-icon.png" class="card-img-top" alt="...">-->
  <!--        <div class="card-body">-->
  <!--          <h5 class="card-title">Card title</h5>-->
  <!--          <p class="card-text">This is a short card.</p>-->
  <!--          <a href="#" class="btn btn-primary">Book</a>-->
  <!--        </div>-->
  <!--      </div>-->
  <!--    </div>-->
  <!--    <div class="col">-->
  <!--      <div class="card h-100">-->
  <!--        <img src="../assets/movie-icon.png" class="card-img-top" alt="...">-->
  <!--        <div class="card-body">-->
  <!--          <h5 class="card-title">Card title</h5>-->
  <!--          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>-->
  <!--          <a href="#" class="btn btn-primary">Book</a>-->
  <!--        </div>-->
  <!--      </div>-->
  <!--    </div>-->
  <!--    <div class="col">-->
  <!--      <div class="card h-100">-->
  <!--        <img src="../assets/movie-icon.png" class="card-img-top" alt="...">-->
  <!--        <div class="card-body">-->
  <!--          <h5 class="card-title">Card title</h5>-->
  <!--          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>-->
  <!--          <a href="#" class="btn btn-primary">Book</a>-->
  <!--        </div>-->
  <!--      </div>-->
  <!--    </div>-->
  <!--  </div>-->

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

const all_Venues = ref(store.state.venues || []);
const is_loading = ref(true);
onBeforeMount(() => {
  if (store.state.venues.length > 0) {
    all_Venues.value = store.state.venues;
    is_loading.value = false;
  } else {
    axios
      .get("/user/getVenues")
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
.card-width{
  width: 130%;
}
</style>
