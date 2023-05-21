import { createStore } from 'vuex'

export default createStore({
  state: {
    user:localStorage.getItem("user")||{},
  },
  getters: {
  },
  mutations: {
    adduser:(state,payload)=>{
      localStorage.setItem("user",JSON.stringify(payload))
      state.user=payload
    },

    removeuser:(state)=>{
      state.user={}
      localStorage.removeItem("user")
    }
  },
  actions: {
  },
  modules: {
  }
})
