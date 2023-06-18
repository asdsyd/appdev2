<template>
  <user-nav-bar/>
<div v-if="!is_loading">
  <h1>{{ venue.name }}</h1>
  <hr>
  <hr>
  <p>{{ venue.name }} is a theatre located in {{ venue.place }} of {{ venue.location }}</p>
  <hr>
  <p>{{ venue.name  }} has a capacity of {{ venue.capacity }}</p>
  <hr>
  <p>
    for bookings check the daashboard to find this theatre to book your favourite shows
  </p>
  <p>happy entertainment!!</p>
</div>

  <user-bottom-nav-bar/>
</template>
<script setup>
import UserNavBar from "@/views/UserNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
const isloading = ref(true);
const venue_Id = ref(router.currentRoute.value.params.Venue);
const store = useStore();
const venue = reactive({
  name: "",
  place: "",
  location: "",
  capacity: null,
});
onBeforeMount(() => {
  axios
    .get("/admin/" + venue_Id.value + "/getVenuedata")
    .then((res) => {
      const { name, place, location, capacity } = res.data;
      venue.name = name;
      venue.place = place;
      venue.location = location;
      venue.capacity = capacity;
      isloading.value=false
    })
    .catch((e) => {
      console.log(e);
    });
});
</script>