<template>
  <user-nav-bar/>
<div v-if="!is_loading">
  <h1><b>{{ venue.name }}</b></h1>
<br>
<br>
  <p><b>{{ venue.name }}</b> is a theatre located in <b>{{ venue.place }}</b> in the city of {{ venue.location }}</p>
  <p><b>{{ venue.name }}</b> has a capacity of {{ venue.capacity }}</p>
  <p>
    for bookings check the dashboard to find this theatre to book your favourite shows
  </p>
  <p>happy entertainment!!</p>
</div>

  <user-bottom-nav-bar/>
</template>
<script setup>
import {ref,reactive,onBeforeMount} from 'vue'
import router from '@/router';
import axios from '@/axios';
import UserNavBar from "@/views/UserNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
const is_loading = ref(true);
const venue_Id = ref(router.currentRoute.value.params.Venue);

const venue = reactive({
  name: "",
  place: "",
  location: "",
  capacity: null,
});
onBeforeMount(() => {
  axios
    .get("/user/" + venue_Id.value + "/getvenue")
    .then((res) => {
      const { name, place, location, capacity } = res.data;
      venue.name = name;
      venue.place = place;
      venue.location = location;
      venue.capacity = capacity;
      is_loading.value=false
    })
    .catch((e) => {
      console.log(e);
    });
});
</script>