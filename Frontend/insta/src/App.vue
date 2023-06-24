<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-3">
      
      <router-link :to="{ name:'home' }">
        <a class="navbar-brand">
          <img class="insta-icon" src="@/assets/logo.png">
          | Juyeonistagram
        </a>
      </router-link>

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <nav class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <!-- <li class="nav-item active">
            <router-link :to="{ name:'home' }" class="nav-link">Home</router-link>
          </li> -->
          <li class="nav-item">
            <router-link :to="{ name:'createpost' }" class="nav-link">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-camera-fill" viewBox="0 0 16 16">
                <path d="M10.5 8.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>
                <path d="M2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4H2zm.5 2a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1zm9 2.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0z"/>
              </svg>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="#" class="nav-link">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-send" viewBox="0 0 16 16">
              <path d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576 6.636 10.07Zm6.787-8.201L1.591 6.602l4.339 2.76 7.494-7.493Z"/>
              </svg>
            </router-link>
          </li>
          <!-- <li class="nav-item">
            <router-link :to="{ name:'home' }" class="nav-link">Followings</router-link>
          </li> -->
        </ul>
      </nav>
    </nav>
    <div v-if="token" class="d-flex justify-content-between">
      <div class="mt-auto mb-auto">
        <h2>Hello!</h2>
        <span>
          {{username}}님, 여기는 긴쥬의 소셜네트워크에요 ❤️💞💓💝💘
        </span>
      </div>
      <div class="mt-auto mb-0">
        <router-link :to="{ name:'profile', params: {user : username}  }">
          <button type="submit" class="btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-house" viewBox="0 0 16 16">
            <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5ZM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5 5 5Z"/>
            </svg>
          </button>
        </router-link>
        <!-- <router-link :to="{ name:'changepw' }">
          <button type="submit" class="btn btn-primary">Change PW</button>
        </router-link> -->
          

        <button @click="logout" type="submit" class="">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-box-arrow-right" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"/>
          <path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
          </svg>
        </button>
      </div>
    </div>
    <hr>
      <router-view/>
  </div>

</template>

<script>

export default {
  name: 'App',
  computed: {
    token(){
      return this.$store.state.token
    },
    username(){
      return this.$store.state.username
    },
  },
  methods: {
    logout(){
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style scoped>
.btn {
  width: 7rem;
  height: 2.5rem;
  background-color: #fff;
  color: rgb(133, 187, 186);
  border: none;
}
.btn:hover {
  color: rgb(16, 52, 82);
  background-color: #fff;
}
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
.insta-icon{
  width: 30px;
  height: 30px;
}

</style>