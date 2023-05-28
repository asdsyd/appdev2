<template>
  <UserNavBar/>
  <UserBottomNavBar/>
</template>
<script>
import {defineComponent} from "vue";
import UserNavBar from "@/views/UserNavBar.vue";
import router from "@/router";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";

export default defineComponent({
  components: {UserBottomNavBar, UserNavBar}
})
const logout = ()=>{
  store.commit('removeuser')
  router.push('/user/login')
}
</script>