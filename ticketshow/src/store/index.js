import { createStore } from 'vuex'

export default createStore({
  state: {
    user:JSON.parse(localStorage.getItem("user"))||{},
    venues:[]
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
    },
    addvenues:(state,payload)=>{
      state.venues=payload
    }
    

  },
  actions: {
  },
  modules: {
  }
})
