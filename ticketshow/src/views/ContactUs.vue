<script setup>

import UserNavBar from "@/views/UserNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
</script>

<template>
  <user-nav-bar />

  <div class=" mb-3 container display-3 rounded-pill border border-success ">Contact Us</div>
  <div class="container my-5">
    <div class="row justify-content-center">
      <div class="col-lg-9">
        <form>
          <div class="row g-3">
            <div class="col-md-6">
              <label for="your-name" class="form-label">First Name</label>
              <input type="text" class="form-control rounded-pill" id="your-name" name="your-name" required placeholder="Asad">
            </div>
            <div class="col-md-6">
              <label for="your-surname" class="form-label">Last Name</label>
              <input type="text" class="form-control rounded-pill" id="your-surname" name="your-surname" required placeholder="Sayeed">
            </div>
            <div class="col-md-6">
              <label for="your-email" class="form-label">Your Email</label>
              <input type="email" class="form-control rounded-pill" id="your-email" name="your-email" required placeholder="example@gmail.com">
            </div>
            <div class="col-md-6">
              <label for="your-subject" class="form-label">Subject</label>
              <input type="text" class="form-control rounded-pill" id="your-subject" name="your-subject" placeholder="Subject...">
            </div>
            <div class="col-12">
              <label for="your-message" class="form-label">Message</label>
              <textarea class="form-control" id="your-message" name="your-message" rows="5" required placeholder="Enter your message..."></textarea>
            </div>
            <div class="col-12">
              <div class="row">
                <div class="col-md-6">
                  <button data-res="<?php echo $sum; ?>" type="submit" class=" rounded-pill btn btn-dark w-100 fw-bold" >Send</button>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>

  <footer class="page-footer">
    <span>made by </span>
    <a href="https://georgemartsoukos.com/" target="_blank">
      <img width="24" height="24" src="https://assets.codepen.io/162656/george-martsoukos-small-logo.svg" alt="George Martsoukos logo">
    </a>
  </footer>

  <user-bottom-nav-bar/>
</template>

<style scoped>
body {
  background: #fafbfb;
}


/* FOOTER STYLES
–––––––––––––––––––––––––––––––––––––––––––––––––– */
.page-footer {
  position: fixed;
  right: 0;
  bottom: 50px;
  display: flex;
  align-items: center;
  padding: 5px;
  z-index: 1;
}

.page-footer a {
  display: flex;
  margin-left: 4px;
}
</style>