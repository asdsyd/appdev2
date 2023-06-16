<template>

  <nav-bar/>

  <div>
    <canvas id="myChart"></canvas>
  </div>

  <user-bottom-nav-bar/>

</template>
<script>

import {defineComponent} from "vue";
import NavBar from "@/views/NavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";

export default defineComponent({
  components: {UserBottomNavBar, NavBar}
})
</script>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});
</script>