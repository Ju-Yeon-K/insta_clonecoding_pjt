<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-3">
      
      <router-link :to="{ name:'home' }">
        <a class="navbar-brand">
          🦜 | Juyeonistagram
        </a>
      </router-link>

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <nav class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <router-link :to="{ name:'home' }" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name:'createpost' }" class="nav-link">New Post</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name:'profile' }" class="nav-link">Profile</router-link>
          </li> 
          <li class="nav-item">
            <router-link :to="{ name:'home' }" class="nav-link">Likes</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name:'home' }" class="nav-link">Followings</router-link>
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
};
</script>

<style scoped>
*{
  text-decoration: none;
}
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