<template>
  <user-logged-nav-bar/>
  <div class="accordion" id="accordionExample">
    <div class="accordion-item">
      <h2 class="accordion-header">
        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
          Venue #1
        </button>
      </h2>
      <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
        <div class="accordion-body">
          <div class="row row-cols-1 row-cols-md-3 g-4 container">
            <div class="col">
              <div class="card h-100">
                <img src="../assets/movie-icon.png" class="card-img-top" alt="...">
                <div class="card-body">
                  <h5 class="card-title">Card title</h5>
                  <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                  <a href="#" class="btn btn-primary">Book</a>
                </div>
              </div>
            </div>
            <div class="col">
              <div class="card h-100">
                <img src="../assets/movie-icon.png" class="card-img-top" alt="...">
                <div class="card-body">
                  <h5 class="card-title">Card title</h5>
                  <p class="card-text">This is a short card.</p>
                  <a href="#" class="btn btn-primary">Book</a>
                </div>
              </div>
            </div>
          </div>








          <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
        </div>
      </div>
    </div>
    <div class="accordion-item">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
          Accordion Item #2
        </button>
      </h2>
      <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
        <div class="accordion-body">
          <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
        </div>
      </div>
    </div>
    <div class="accordion-item">
      <h2 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
          Accordion Item #3
        </button>
      </h2>
      <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
        <div class="accordion-body">
          <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
        </div>
      </div>
    </div>
  </div>


<!--  <div class="row row-cols-1 row-cols-md-3 g-4 container">-->
<!--    <div class="col">-->
<!--      <div class="card h-100">-->
<!--        <img src="../assets/movie-icon.png" class="card-img-top" alt="...">-->
<!--        <div class="card-body">-->
<!--          <h5 class="card-title">Card title</h5>-->
<!--          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>-->
<!--          <a href="#" class="btn btn-primary">Book</a>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div class="col">-->
<!--      <div class="card h-100">-->
<!--        <img src="../assets/movie-icon.png" class="card-img-top" alt="...">-->
<!--        <div class="card-body">-->
<!--          <h5 class="card-title">Card title</h5>-->
<!--          <p class="card-text">This is a short card.</p>-->
<!--          <a href="#" class="btn btn-primary">Book</a>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div class="col">-->
<!--      <div class="card h-100">-->
<!--        <img src="../assets/movie-icon.png" class="card-img-top" alt="...">-->
<!--        <div class="card-body">-->
<!--          <h5 class="card-title">Card title</h5>-->
<!--          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>-->
<!--          <a href="#" class="btn btn-primary">Book</a>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div class="col">-->
<!--      <div class="card h-100">-->
<!--        <img src="../assets/movie-icon.png" class="card-img-top" alt="...">-->
<!--        <div class="card-body">-->
<!--          <h5 class="card-title">Card title</h5>-->
<!--          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>-->
<!--          <a href="#" class="btn btn-primary">Book</a>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->


  <UserBottomNavBar/>
</template>
<script>
import {defineComponent} from "vue";
import UserNavBar from "@/views/UserNavBar.vue";
import router from "@/router";
import UserBottomNavBar from "@/views/UserBottomNavBar.vue";
import UserLoggedNavBar from "@/views/UserLoggedNavBar.vue";
import store from "@/store";


const all_Venues = ref(store.state.venues||null)
const is_loading = ref(false)
onBeforeMount(()=>{
  if(store.state.venues){
    all_Venues.value = store.state.venues
  }else{
    axios.get('/user/getVenues').then(res=>{
      const {venues} = res.data
      venues.forEach(e=>{
        e.movies.forEach(l=>{
          const c = new Date(l.end)
          c.setHours(c.getHours()-5)
          c.setMinutes(c.getMinutes()-30)
          const f = new Date(l.start)
          f.setHours(f.getHours()-5)
          f.setMinutes(f.getMinutes()-30)
          l.start=f
          l.end=c
        })
      })
      store.commit("addvenues",venues)
    })
  }

})
const logout = ()=>{
  store.commit('removeuser')
  router.push('/user/login')
}
</script>