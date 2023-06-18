<template>
  <user-nav-bar/>
  <div class="container mt-4">
    <div>
    <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" placeholder="Old Password">

    </div>
    <div>
    <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" placeholder="New Password">

    </div>
    <div>
    <input class="rounded-pill col-3 m-2 py-1 border-warning-subtle" placeholder="Confirm New Password">

    </div>
    <button class="btn btn-warning rounded-pill col-3 m-2" type="submit">Change Password</button>
  </div>
</template>
<script setup>
import UserNavBar from "@/views/UserNavBar.vue";
</script>