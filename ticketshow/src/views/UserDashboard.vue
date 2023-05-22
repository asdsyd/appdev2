<template>
  <UserNavBar/>
</template>
<script>
import {defineComponent} from "vue";
import UserNavBar from "@/views/UserNavBar.vue";
import router from "@/router";

export default defineComponent({
  components: {UserNavBar}
})
const logout = ()=>{
  store.commit('removeuser')
  router.push('/user/login')
}
</script>