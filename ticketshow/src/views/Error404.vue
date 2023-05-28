<template>

  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Bootstrap 5 404 Error Page</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>


  <body>
  <div class="d-flex align-items-center justify-content-center vh-100">
    <div class="text-center">
      <h1 class="display-1 fw-bold">404</h1>
      <p class="fs-3 display-1"> <span class="text-danger">Opps!</span> Page not found.</p>
      <p class="lead">
        The page you’re looking for doesn’t exist likely due to incorrect URL.
      </p>
      <router-link :to="getHomeLink()" class="btn btn-primary rounded-5">Go Home</router-link>
    </div>
  </div>
  </body>

  <UserBottomNavBar/>



<!--  <div>-->
<!--    <h1 class="display-1 text-danger text-center">Error 404 - Page Not Found</h1>-->
<!--    <p class="display-5">The requested URL does not exist.</p>-->
<!--  </div>-->
</template>

<script >
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";

export default {
  name: 'ErrorComponent',
  components: {UserBottomNavBar},
  methods: {
    getHomeLink() {
      const userRole = 'user';
      if (userRole === 'user') {
        return { name: 'UserDashboard' };
      } else if (userRole === 'admin') {
        return { name: 'AdminDashboard' };
      } else {
        return { name: 'Home' };
      }
    }
  }
}
</script>

<style>
/* Add any necessary styles for the error component */
</style>
