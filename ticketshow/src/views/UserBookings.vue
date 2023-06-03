<template>
  <UserNavBar/>

  <div class="outer">
    <div class="inner">
      <div class="textss">
        venue_! - show_1 8 pm - 9pm
      </div>
      <div >
        <button class="btn btn-success bt">rate</button>
      </div>
    </div>
  </div>
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