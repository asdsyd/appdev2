
<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">{{$store.state.user.username}} Dashboard</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Summary</a>
          </li>
        </ul>
        <button class="btn btn-outline-success" type="submit">Logout</button>
      </div>
    </div>
  </nav>
  <div class="m-lg-3 card mb-3 border-primary" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Venue_01</h5>
      <p class="card-text">No shows created</p>
      <div>
        <button class=" m-3 rounded-circle btn btn-primary">+</button>
      </div>
      <button href="#" class="me-3 btn btn-warning">Edit</button>
      <button href="#" class="btn btn-danger">Delete</button>
    </div>
  </div>
  <div class="m-lg-3 card mb-3 border-dotted " style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title text-bg-light">New Venue</h5>
      <p class="card-text">Click on the buttion below to add Venue</p>
      <div>
        <button class=" m-3 rounded-circle btn btn-success">+</button>
      </div>
    </div>
  </div>
</template>
<script>
</script>