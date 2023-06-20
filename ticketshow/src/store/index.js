import { createStore } from 'vuex'
export default createStore({
  state: {
    admin: JSON.parse(localStorage.getItem("admin")) || {},
    user: JSON.parse(localStorage.getItem("user")) || {},
    venues: [],
    export_id: JSON.parse(localStorage.getItem("export")) || {},
  },
  getters: {
    getexportid: (state) => state.export_id.task,
  },
  mutations: {
    adduser: (state, payload) => {
      if (localStorage.getItem("user")) {
        localStorage.removeItem("user")
      }
      localStorage.setItem("user", JSON.stringify(payload))
      state.user = payload
    },
    deleteVenue: (state, id) => {
      state.venues = state.venues.filter((e, i) => i !== id)
    },
    addadmin: (state, payload) => {
      if (localStorage.getItem("admin")) {
        localStorage.removeItem("admin")
      }
      localStorage.setItem("admin", JSON.stringify(payload))
      state.admin = payload
    },

    removeuser: (state) => {
      state.user = {}
      localStorage.removeItem("user")
    },
    removeadmin: (state) => {
      state.admin = {}
      localStorage.removeItem("admin")
    },
    addvenues: (state, payload) => {
      state.venues = payload
    },
    removevenues: (state) => {
      state.venues = []
    },
    refresher: (state, payload) => {
      localStorage.setItem("user", JSON.stringify(payload))
      state.user = payload
    },
    refresheradmin: (state, payload) => {
      localStorage.setItem("admin", JSON.stringify(payload))
      state.admin = payload
    },
    addtask: (state, payload) => {
      localStorage.setItem("export", JSON.stringify(payload))
      state.export_id = payload
    },
    removeexport: (state) => {
      localStorage.removeItem("export")
      state.export_id = {}
    }



  },
  actions: {
  },
  modules: {
  }
})

