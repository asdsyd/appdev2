<template>
  <NavBar :is-summary="true" ></NavBar>
  <p> Testing out chart js</p>
  <div>
    <canvas id="myChart"></canvas>
  </div>
  <Bar
      id="my-chart-id"
      :name="name"
      :options="chartOptions"
      :data="chartData"
  />
</template>

<script setup>
import {ref,reactive,onBeforeMount} from 'vue'
import axios from '@/adminaxios'
import NavBar from "@/views/NavBar.vue";
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)


 const name = ref('BarChart')

  
 onBeforeMount(() => {
  axios.get('/admin/summary').then(res=>{
    console.log(res.data)
  }).catch(e=>console.error(e))
 })
    const chartData=reactive( {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
      })
      const chartOptions=reactive ({
        responsive: true
      })
    
  

</script>