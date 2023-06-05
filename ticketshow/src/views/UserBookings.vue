<template>
  <UserNavBar/>

  <div class="outer">
    <div class="inner">
      <div class="textss">
        venue_! - show_1 8 pm - 9pm
      </div>
      <div>
<!--        <button class="px-4 btn rounded-pill btn-outline-success bt" v-if="v.can_rate">rate</button>-->

<!--        Modal trigger-->
        <button type="button" class="px-4 btn rounded-pill btn-outline-success bt" data-toggle="modal" data-target="#exampleModalCenter" v-if="v.can_rate">
          rate
        </button>

        <button class="px-4 btn rounded-pill btn-success disabled bt"  v-else @click="alert('Already rated thank you')" >rated {{v.rating}}</button>

      </div>
    </div>
          <!-- Modal -->

      <div class="text-center" v-else>no bookings made</div>
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
  <UserBottomNavBar/>
</template>
<script setup>
import UserNavBar from "@/views/UserNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
</script>
<style scoped>
.outer{
  margin: 7%;
}
.inner{
  border: 2px solid black;
  width: 100%;
  border-radius: 30px;
  display: flex;
  justify-content: space-between;
  padding: 2%;
}
.textss{
  font-size: 140%;
}
.bt{
  font-size: 140%;
}
@media screen and (max-width:400px) {
  .inner{
    flex-direction: column;
  }
}
</style>