<template>
  <user-nav-bar/>
  <div class="container mt-4">
    <div>
    <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" type="password" v-model="details.oldpassword"
           placeholder="Old Password">

    </div>
    <div>
    <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" type="password" v-model="details.password"
           placeholder="New Password">

    </div>
    <div>
    <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" type="password" v-model="details.retypepassword"
           placeholder="Confirm New Password">

    </div>
    <button class="btn btn-warning rounded-pill col-3 m-2" type="submit" value="Change Password" :disabled="!passwordMatch" submit.prevent>Change Password</button>
  </div>
</template>
<script setup>
import UserNavBar from "@/views/UserNavBar.vue";
import {computed, reactive} from "vue";

const passwordMatch = computed(() => details.password === details.retypepassword)
const details = reactive({
  oldpassword: "",
  password: "",
  retypepassword: "",
});
</script>