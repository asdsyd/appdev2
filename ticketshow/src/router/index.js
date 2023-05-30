import HomeViewVue from "@/views/About.vue";
import axios from "../axios";
import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "@/views/LandingPage.vue";

const routes = [
  {
    path: '/:catchAll(.*)',
    name: "Error404",
    component: () => import("../views/Error404.vue")
  },
  {
    path:'/',
    name:'Homeview',
    component:LandingPage
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
  },
  {
    path: "/admin/login",
    name: "AdminLogin",
    component: () => import("../views/AdminLogin.vue"),
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
  {path:'/admin/:Show/EditShow',
  name:'EditShow',
  component:()=>import('../views/EditShow.vue')
  
  },
  {
    path: "/:username/dashboard",
    name: "UserDashboard",
    component: () => import("../views/UserDashboard.vue"),
    meta:{requiresAuth:true}
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
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
async function isAuth(){

  try{
    const resp = await axios.get('/check')
    if(resp.status===200){
      return true
    }
  }
  catch(err){
    return false
  }
}
async function isAdminAuth(){
  try{
   
    const resp = await axios.get('/admin/check')
    if(resp.status===200){
      return true
    }
  }
  catch(err){
    return false
  }
}

// router.beforeEach(async (to,from,next)=>{

//   const auth = to.matched.some(r=>r.meta.requiresAuth===true)
//   const isadmin_route = to.matched.some(r=>r.meta.AdminRoute)
//   let isAuthorized;
//   if(auth&&isadmin_route){
//     isAuthorized=await isAdminAuth()
//   }
//   else if(auth && isadmin_route === false){
//     isAuthorized=await isAuth()
//   }
//   else{
//     isAuthorized=true
//   }

//   if(isAuthorized===true){
//     next()
//   }else if(isAuthorized===false && isadmin_route===true){
  
//     next('/admin/login')
//   }
//   else{

//     next('/user/login')
//   }
// })
export default router;
