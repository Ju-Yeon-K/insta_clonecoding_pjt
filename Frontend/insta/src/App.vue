<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-3">
      <a class="navbar-brand disabled">
        🦜 | Juyeonistagram
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <nav class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="{% url 'posts:index' %}">Home <span class="sr-only"></span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'posts:create' %}">New Post</a>
          </li>
          <li class="nav-item">

            <a class="nav-link" href="{% url 'profile' request.user.username %}">Profile</a>

          </li> 
          <li class="nav-item">
            <a class="nav-link" href="#">Likes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Followings</a>
          </li>
        </ul>
      </nav>
    </nav>
      <router-view/>
  </div>

</template>

<script>

export default {
  name: 'App',
  data() {

  },
};
</script>

<style scoped>
.buttonpos {
  top:84px;
  left: 80px;
}
img {
  width: 100%;
  height: 100%;
}
.boxing {
  width: 500px;
  height: 500px;
}
.imgbox {
  width: 80px;
  height: 80px;
  border-radius: 100%;
  border:3px solid black;
}
.imgsizing {
  height: 270px;
}
</style>