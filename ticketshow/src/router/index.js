import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
        import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/admin/login",
    name: "AdminLogin",
    component: () => import("../views/AdminLogin.vue"),
  },
  {
    path:"/admin/:username",
    name: "AdminDashboard",
    component: () => import("../views/AdminDashboard.vue")
  },
  {
    path:"/admin/CreateVenue",
    name: "CreateVenue",
    component: () => import("../views/CreateVenue.vue")
  },
  {
    path: "/admin/:Venue/CreateShow",
    name: "CreateShow",
    component: () => import("../views/CreateShow.vue")
  },
  {
    path: "/admin/:username/AdminSummary",
    // name: "AdminSummary",
    component: () => import("../views/Summary.vue")
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
  {
    path: "/user/dashboard",
    name: "UserDashboard",
    component: () => import("../views/UserDashboard.vue")
  },
  {
    path: "/user/bookings",
    name: "UserBookings",
    component: () => import("../views/UserBookings.vue")
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
