<template>
  <UserLoggedNavBar/>


    <div>
      <ProfileCard v-if="!self"
                   :username="username"
                   :bio="bio"
      />
      <ProfileCard v-else
                   :username="$store.state.username"
                   :bio="$store.state.bio"
                   :avatar="$store.state.avatar"
                   profile_page=true
      />

    </div>


  <UserBottomNavBar/>
</template>
<script setup>
import UserNavBar from "@/views/UserNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
</script>