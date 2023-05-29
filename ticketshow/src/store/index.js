import { createStore } from 'vuex'
export default createStore({
  state: {
    user:JSON.parse(localStorage.getItem("user"))||{},
    venues:[],
  },
  getters: {


  },
  mutations: {
    adduser:(state,payload)=>{
        if(localStorage.getItem("user")){
            localStorage.removeItem("user")
        }
      localStorage.setItem("user",JSON.stringify(payload))
      state.user=payload
    },
deleteVenue:(state,id)=>{
state.venues=state.venues.filter((e,i)=>i!==id)
},

    removeuser:(state)=>{
      state.user={}
      localStorage.removeItem("user")
    },
    addvenues:(state,payload)=>{
      state.venues=payload
    },
    refresher:(state,payload)=>{
      const {accessToken,...rest} = state.user
      state.user = {accessToken,payload}
    },

  },
  actions: {
    getvenues:({commit})=>{

    }

    },
  modules: {
  }
})

