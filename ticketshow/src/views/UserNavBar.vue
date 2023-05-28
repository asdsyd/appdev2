<template>

<UserLoggedNavBar/>

</template>
<script setup>
import store from '@/store';
import router from '@/router';
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
const logout = () => {
  store.commit("removeuser");
  router.push("/user/login");
};
</script>