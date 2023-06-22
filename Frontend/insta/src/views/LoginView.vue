<template>
  <div class="d-flex justify-content ms-5 mt-5">
    <div class="mt-auto mb-auto">

    <h1 class="title mb-2">
        Log In
    </h1>
      <div class="container position-relative">

      <div class="row mb-3 g-3 d-flex justify-content-between">
        <div class="col-auto">
          <label  for="username" class="col-form-label title-init">아이디</label>
        </div>
        <div class="col-auto">
          <input type="username" id="username" class="form-control" v-model="username">
        </div>
      </div>


      <div class="row mb-3 g-3 d-flex justify-content-between">
        <div class="col-auto">
          <label  for="password" class="col-form-label title-init">비밀번호</label>
        </div>
        <div class="col-auto ">
          <input type="password" id="password" class="form-control" v-model="password" @keyup.enter="login">
        </div>
      </div>

      <div class="row mb-3 g-3 d-flex justify-content-between">
        <div class="col-auto">
          <router-link :to="{ name:'signup' }">
            <button class="btn btn-success title-init">Sign up</button>
          </router-link> 
        </div>

        <div class="col-auto">
          <input class="btn btn-primary title-init" type="button" value="LogIn" @click.prevent="login">
        </div>
      </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password
      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    },
  }
}
</script>

<style scoped>
.btn {
  width: 10rem;
  height: 2.5rem;
  margin: 0.5rem;
  background-color: rgb(13, 13, 32);
  border: solid 0px rgb(161, 127, 133);
}
.btn:hover {
  color: rgb(20, 148, 146);
  background-color: rgb(41, 41, 55);
}
</style>