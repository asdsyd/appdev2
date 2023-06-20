<template>

    <nav-bar/>

  <div class="custom" v-if="task_obj">
    <h2>venue id :-  {{task_obj.task}}</h2>
    <button @click="fetchcsv">export csv</button>
  </div>

  <div v-else>no export task assigned</div>

    <user-bottom-nav-bar/>
</template>

<script setup>
import {ref } from 'vue'
import axios from "@/adminaxios"
import NavBar from "@/views/NavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import { useStore } from "vuex";
import router from '@/router';

const store = useStore()
const task_obj = ref(Object.keys(store.state.export_id).length>0?store.state.export_id:null)

const fetchcsv = ()=>{
  axios({
  url: '/admin/export/results/' + task_obj.value.task_id,
  method: 'GET',
  responseType: 'blob',
})
  .then(response => {
  if(response.status === 102){
    throw Error("working")
  }
  
      const url = window.URL.createObjectURL(new Blob([response.data]));
      
  
      const tempLink = document.createElement('a');
      tempLink.href = url;
      tempLink.setAttribute('download', 'export.csv'); 
      tempLink.click();
      
      
      window.URL.revokeObjectURL(url);
      store.commit("removeexport");
      setTimeout(()=>router.push('/admin/'+store.state.admin.username),3000)
  })
  .catch(error => {
  alert("work in progress")
  });

}
</script>

