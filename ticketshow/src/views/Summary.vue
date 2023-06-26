<template>
  <NavBar :is-summary="true"></NavBar>
  <div v-show="!is_loading" class="container">
    <p class="mt-3 display-6"> Admin Venue Summary</p>

    <Bar v-for="v in summarydata" id="my-chart-id" :options="chartOptions" :data="v.data" class="chart-container m-5 py-3" />
  </div>
</template>

<script setup>
import { ref, reactive, onBeforeMount } from 'vue'
import axios from '@/adminaxios'
import NavBar from "@/views/NavBar.vue";
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)


const is_loading = ref(true)

onBeforeMount(() => {
  axios.get('/admin/summary').then(res => {
    const { data } = res.data


    for (const { id, name, movies } of data) {
      const arr = {
        id: id,
        data: {
          labels: movies.map(l => l.name),
          datasets: [{
            label: name, data: movies.map(l => l.bookings),
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(255, 205, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(201, 203, 207, 0.2)'
            ],
            barPercentage: 0.13
          }],
        },


      }
      summarydata.value.push(arr)
    }
    console.log(summarydata.value)
    is_loading.value = false
  }).catch(e => console.error(e))
})

const summarydata = ref([])
const chartOptions = reactive({
  responsive: true,
  scales: {
      y: {
        beginAtZero: true,
        // ticks: {
        //   stepSize: 2
        // },
        padding: {
          bottom: 10 // Add 10 pixels of padding at the bottom of the y-axis
        },
        title:{
          display:true,
          text:"TOTAL BOOKINGS"
        }
      },
      x: {
        title: {
          display: true,
          text: 'MOVIES'
        },
        beginAtZero: true
      }
    }

})




</script>
<style>
.chart-container {
  width: 300px; /* Adjust the width as needed */
  height: 200px; /* Adjust the height as needed */
}
</style>