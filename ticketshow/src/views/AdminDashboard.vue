
<template>
  <NavBar></NavBar>

  <div v-if="venues"  v-for="v in venues" class="m-lg-3 card mb-3 border-primary" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Venue_01</h5>
      <p class="card-text">No shows created</p>
      <div>
        <button class=" m-3 rounded-circle btn btn-primary">+</button>
      </div>
      <button class="btn btn-success">Edit</button>
      <button href="#" class="btn btn-danger">Delete</button>
    </div>
  </div>
  <div class="m-lg-3 card mb-3 border-dotted " style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title text-bg-light">New Venue</h5>
      <p class="card-text">Click on the buttion below to add Venue</p>
      <div>
        <button class=" m-3 rounded-circle btn btn-success">+</button>
      </div>
    </div>
  </div>
</template>
<script setup>
import {ref} from "vue";
import NavBar from "@/views/NavBar.vue";
import { useStore } from 'vuex';
import axios from '../axios';
</script>