<template>
  <UserNavBar />

  <div class="outer" v-show="!is_loading">
    <div class="inner" v-if="all_bookings.length > 0" v-for="v in all_bookings">
      <div class="textss">
        {{ v.venue }} {{ v.movie }} {{ FormatTime(v.start) }} -
        {{ FormatTime(v.end) }}
      </div>
      <div>
        <!--        <button class="px-4 btn rounded-pill btn-outline-success bt" v-if="v.can_rate">rate</button>-->

        <!--        Modal trigger-->
        <button
          class="px-4 btn rounded-pill btn-outline-success bt"
          type="button"
          v-if="v.can_rate"
          @click="toggleModal({to:'show',id:v.id})"
        >
          rate
        </button>

        <button
          class="px-4 btn rounded-pill btn-success disabled bt"
          v-else
          @click="alert('Already rated thank you')"
        >
          rated {{ v.rating }}
        </button>
      </div>
    </div>

    <div class="text-center" v-if="all_bookings.length === 0">
      no bookings made
    </div>
  </div>

  <div
    class="modal"
    id="exampleModal"
    v-show="rating_toggle"
    style="display: block"
    role="dialog"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
          <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
            @click="toggleModal({to:'close'})"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <select v-model="rating">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
          </select>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-dismiss="modal"
            @click="toggleModal({to:'close'})"
          >
            Close
          </button>
          <button type="button" class="btn btn-primary" @click="rate">
            Rate
          </button>
        </div>
      </div>
    </div>
  </div>

  <!--  -->
  <!--    <div class="container py-3 rounded-pill border border-success-subtle  justify-content-between position-relative">-->
  <!--      <span class="h4 position-absolute start-10 ">-->
  <!--                venue_! - show_1 8 pm - 9pm {{"arbaz"}}-->
  <!--      </span>-->
  <!--      <span >-->
  <!--        <button class="px-4 btn rounded-pill btn-success disabled bt" @click="alert('Already rated thank you')" >rated</button>-->
  <!--      </span>-->
  <!--      <span >-->
  <!--        <button class="px-4 btn rounded-pill btn-outline-success bt">rate</button>-->
  <!--      </span>-->
  <!--    </div>-->
  <UserBottomNavBar />
</template>
<script setup>
import UserNavBar from "@/views/UserNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import { onBeforeMount } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import axios from "@/axios";
import { ref } from "vue";

const store = useStore();
const rating = ref(null);
const movie_to_rate = ref(null)
const is_loading = ref(true);
const rating_toggle = ref(false);
const toggleModal = (opt) => {
  if (opt.to === "show") {
    rating_toggle.value = true;
    movie_to_rate.value=opt.id  
  } else {
    rating_toggle.value = false;
    movie_to_rate.value=null
  }
};

const HourFomatterObj = {
  "00": ["12", "AM"],
  "01": ["1", "AM"],
  "02": ["2", "AM"],
  "03": ["3", "AM"],
  "04": ["4", "AM"],
  "05": ["5", "AM"],
  "06": ["6", "AM"],
  "07": ["7", "AM"],
  "08": ["8", "AM"],
  "09": ["9", "AM"],
  10: ["10", "AM"],
  11: ["11", "AM"],
  12: ["12", "NOON"],
  13: ["1", "PM"],
  14: ["2", "PM"],
  15: ["3", "PM"],
  16: ["4", "PM"],
  17: ["5", "PM"],
  18: ["6", "PM"],
  19: ["7", "PM"],
  20: ["8", "PM"],
  21: ["9", "PM"],
  22: ["10", "PM"],
  23: ["11", "PM"],
};
const FormatTime = (time) => {
  const timearr = time.split(" ");
  timearr.shift();
  timearr.pop();
  let timestr = `${timearr[0]} ${timearr[1]} `;
  const Hour = HourFomatterObj[timearr[3].slice(0, 2)];
  const Time = timearr[3].slice(3, 5);
  timestr = timestr + `${Hour[0]}:${Time} ${Hour[1]}`;
  return timestr;
  // 2023-05-30T22:29
};
const router = useRouter();

const rate = () => {
  
 
  axios
    .post("/user/"+ movie_to_rate.value+"/rating", { rating:Number(rating.value) })
    .then((res) => {toggleModal({to:'close'})
    console.log(res)
})
    .catch((e) => console.log(e));
};

const all_bookings = ref([]);

onBeforeMount(() => {
  axios
    .get("/user/bookings")
    .then((res) => {
      console.log(res.data)
      if (Array.isArray(res.data)) {
        all_bookings.value = res.data;
      } else {
        all_bookings.value = [];
      }
console.log(all_bookings.value)
      is_loading.value = false;
    })
    .catch((err) => console.log(err));
});
</script>
<style scoped>
.outer {
  margin: 7%;
}
.inner {
  border: 2px solid black;
  width: 100%;
  border-radius: 30px;
  display: flex;
  justify-content: space-between;
  padding: 2%;
}
.textss {
  font-size: 110%;
}
.bt {
  font-size: 140%;
}
@media screen and (max-width: 400px) {
  .inner {
    flex-direction: column;
  }
}
</style>
