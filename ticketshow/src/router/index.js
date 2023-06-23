import HomeViewVue from "@/views/About.vue";
import axios from "../axios";
import adminaxios from '@/adminaxios'
import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "@/views/LandingPage.vue";
import store from "@/store";

const routes = [
  {
    path: '/:catchAll(.*)',
    name: "Error404",
    component: () => import("../views/Error404.vue")
  },
  {
    path: "/adminexports",
    name: "Exports",
    component: () => import("../views/Export.vue"),
    meta:{requiresAuth:true,AdminRoute:true}
  },
  {
    path:'/',
    name:'Homeview',
    component:LandingPage
  },
  {path:"/user/:Venue/:Show/book",
  name:"Booking",
    component:()=> import("../views/Book.vue"),
    meta:{requiresAuth:true}
  },
  {

    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
        import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/superAdmin/register",
    name: "AdminRegister",
    component: () => import("../views/AdminRegister.vue"),
    meta:{requiresAuth:true,AdminRoute:true}
  },
  {
    path: "/admin/login",
    name: "AdminLogin",
    component: () => import("../views/AdminLogin.vue")
  },
  {
    path:"/admin/:username",
    name: "AdminDashboard",
    component: () => import("../views/AdminDashboard.vue"),
    meta:{requiresAuth:true,AdminRoute:true}
   
  },
  {
    path:"/admin/CreateVenue",
    name: "CreateVenue",
    component: () => import("../views/CreateVenue.vue"),
    meta:{requiresAuth:true,AdminRoute:true}
  },
  {
    path: "/admin/:Venue/CreateShow",
    name: "CreateShow",
    component: () => import("../views/CreateShow.vue"),
    meta:{requiresAuth:true,AdminRoute:true}
  },
  {
    path: "/admin/:Venue/EditVenue",
    name: "EditVenue",
    component: () => import("../views/EditVenue.vue"),
    meta: {requiresAuth: true, AdminRoute: true},
  },
  {
    path: "/admin/:username/AdminSummary",
    name: "AdminSummary",
    component: () => import("../views/Summary.vue"),
    meta:{requiresAuth:true,AdminRoute:true}
  },
  {
    path: "/user/login",
    name: "UserLogin",
    component: () => import("../views/UserLogin.vue"),
  },
  {
    path: "/user/register",
    name: "UserRegister",
    component: () => import("../views/UserRegister.vue"),
  },
  {path:'/admin/:Venue/:Show/EditShow',
  name:'EditShow',
  component:()=>import('../views/EditShow.vue'),
  meta:{requiresAuth:true,AdminRoute:true}
  
  },
  {
    path: "/user/dashboard",
    name: "UserDashboard",
    component: () => import("../views/UserDashboard.vue"),
  },
  {
    path: "/:username/bookings",
    name: "UserBookings",
    component: () => import("../views/UserBookings.vue"),
    meta:{requiresAuth:true}
  },
  {
    path: "/:username/profile",
    name: "UserProfile",
    component: () => import("../views/UserProfile.vue"),
    meta: {requiresAuth: true}
  },
  {
    path: "/features",
    name: "Features",
    component: () => import("../views/Features.vue"),
  },
  {
    path: "/contactUs",
    name: "ContactUs",
    component: () => import("../views/ContactUs.vue"),
  },
  {
    path: "/search",
    name: "Search",
    component: () => import("../views/MovieSearch.vue")
  },
  {
    path: "/:username/changePassword",
    name: "Password",
    component: () => import("../views/UserPasswordChange.vue"),
    meta:{requiresAuth:true}
  },
  {
    path: "/:Venue/details",
    name: "Venue",
    component: () => import("../views/Venue.vue")
  },
  {
    path: "/:username/updateProfile",
    name: "UpdateProfile",
    component: () => import("../views/UserEditProfile.vue"),
    meta: {requiresAuth: true}
  }

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
async function isAuth(){

  try{
    const resp = await axios.get('/check')
  return true
  }
  catch(err){
    return false
  }
}
async function isAdminAuth(){
  try{   
    const resp = await adminaxios.get('/admin/check')
      return true
  }
  catch(err){
    return false
  }
}

router.beforeEach(async (to,from,next)=>{

  const auth = to.matched.some(r=>r.meta.requiresAuth===true)
  const isadmin_route = to.matched.some(r=>r.meta.AdminRoute===true)
  let isAuthorized;
  if(auth&&isadmin_route){
    isAuthorized=await isAdminAuth()
  }
  else if(auth && isadmin_route === false){
    isAuthorized=await isAuth()
  }
  else{
    isAuthorized=true
  }

  if(isAuthorized===true){
    next()
  }else if(isAuthorized===false && isadmin_route===true){
  store.commit("removeadmin")
  store.commit("removeuser")
    next('/admin/login')
  }
  else{
  store.commit("removeadmin")
  store.commit("removeuser")
    next('/user/login')
  }
})
export default router;
