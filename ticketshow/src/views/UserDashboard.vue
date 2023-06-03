<template>
  <user-nav-bar />
  <div v-if="all_Venues && !is_loading" class="accordion" id="accordionExample">
    <div v-for="v in all_Venues" class="accordion-item">
      <h2 class="accordion-header">
        <button
          class="accordion-button"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#collapseOne"
          aria-expanded="true"
          aria-controls="collapseOne"
        >
          {{ v.name }}
        </button>
      </h2>
      <div
        id="collapseOne"
        class="accordion-collapse collapse show"
        data-bs-parent="#accordionExample"
      >
        <div class="accordion-body">
          <div class="row row-cols-1 row-cols-md-3 g-4 container">
            <div v-if="v.movies" v-for="c in v.movies" lass="col">
              <div class="card h-100">
                <img
                  v-if="c.image"
                  :src="'http://localhost:8000/image/' + c.image"
                  class="card-img-top"
                  alt="movie_image"
                />
                <img
                  v-else
                  src="../assets/movie-icon.png"
                  class="card-img-top"
                  alt="..."
                />
                <div class="card-body">
                  <h5 class="card-title">{{ c.movie_name }}</h5>
                  <p class="card-text">{{ c.description }}</p>
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
    </div>
  </div>

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

const all_Venues = ref(store.state.venues || null);
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
        console.log(venues);
        venues.forEach((e) => {
          e.movies.forEach((l) => {
            const c = new Date(l.end);
            c.setHours(c.getHours() - 5);
            c.setMinutes(c.getMinutes() - 30);
            const f = new Date(l.start);
            f.setHours(f.getHours() - 5);
            f.setMinutes(f.getMinutes() - 30);
            l.start = f;
            l.end = c;
          });
        });

        store.commit("addvenues", venues);
        all_Venues.value = store.state.venues;
        is_loading.value = false;
      })
      .catch((err) => console.log(err));
  }
  console.log(all_Venues.value);
});
const logout = () => {
  store.commit("removeuser");
  router.push("/user/login");
};
</script>
