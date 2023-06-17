<template>
  <user-nav-bar />
  <div class="topdiv" v-if="!is_loading">
    <div>
      Booking - {{ venue_and_show }}
    </div>
    <div>
      Time :- {{ time_of_show }}
    </div>
  </div>


  <form v-if="!is_loading" @submit.prevent="HandleSubmit()">
    <div v-if="err" class="alert alert-danger " role="alert">
      {{ err }}
    </div>
    <div v-if="success" class="alert alert-success " role="alert">
      {{ success }}
    </div>
    <div>
      Available-Seats: {{ available_seats }}
    </div>
    <div class="mt-4 mb-3 col-3 container ">
      <label>Number of Seats</label>
      <input  class="container col-3 form-control rounded-pill" type="number" v-model="number" placeholder="Number of Seats" min="1" :max="available_seats" />
    </div>
    <div class="mt-3 mb-3 col-3 container">
      <label>Price</label>
      <input  readonly class="container col-3 form-control rounded-pill" type="text" v-model="price" placeholder="price" />
    </div>
    <div class="mt-3 mb-3 col-3 container">
      <label>Total Price</label>
      <input  readonly class="container col-3 form-control rounded-pill" type="text" v-model="Totalprice" placeholder="Total price" />
    </div>
    <div class="mt-3 col-3 container">
      <input class="container mb-3 px-4 btn btn-outline-primary rounded-pill" type="submit" value="Confirm Booking" placeholder="Book" />
    </div>
   

  </form>


  <user-bottom-nav-bar />
</template>

<script setup>
import { computed, onBeforeMount, ref } from "vue";
import UserNavBar from "@/views/UserNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import axios from "@/axios";
import router from "@/router";


const FormatTime = (time) => {
  const timearr = time.split(" ");
  timearr.shift();
  timearr.pop();
  let timestr = `${timearr[0]}th ${timearr[1]} ${
    timearr[2]
  } `;
  const Hour =HourFomatterObj[timearr[3].slice(0,2)]
  const Time = timearr[3].slice(3,5)
  timestr = timestr + `${Hour[0]}:${Time} ${Hour[1]}` 

  
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
const success = ref(null)
const err= ref(null)
const is_loading = ref(true)
const number  = ref(1)
const price =  ref(null)
const Totalprice = computed(()=>{if(price){return number.value*Number(price.value)}else{ return null}
})
const available_seats = ref(null)
const venue_and_show = ref(null)
const time_of_show = ref(null)
const venue = router.currentRoute.value.params.Venue
const Show = router.currentRoute.value.params.Show
onBeforeMount(()=>{
axios.get('/user/'+ Show+'/getShow').then(res=>{
const [name,ticketPrice,startTime,endTime,theatre_name,avail_seats] = res.data
venue_and_show.value = `${theatre_name} - ${name}`
price.value=ticketPrice
available_seats.value=avail_seats
time_of_show.value = `${FormatTime(startTime)} - ${FormatTime(endTime)}`
is_loading.value=false
}).catch(err=>{
console.log(err)
})
})

const HandleSubmit=()=>{
  axios.post('/admin/' +venue +'/'+ Show+ '/book',{"number":number.value}).then(res=>{
err.value = null
    success.value = res.data.message
setTimeout(()=>{
  router.push('/user/dashboard')
},2000)
  }).catch(error=>{
    if(error.response.data){
      success.value = null
      err.value=error.response.data.message
    }
  })
}
</script>
<style scoped>
form{
  margin-top: 5%;
}
.topdiv{
  margin-top: 2%;
  display: flex;
  justify-content: space-around;
}
</style>