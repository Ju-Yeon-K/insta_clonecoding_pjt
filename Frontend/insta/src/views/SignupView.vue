<template>
  <div class="d-flex justify-content ms-5 mt-5">
    <div class="mt-auto mb-auto">

    <h1 class="title mb-2">
        Sign Up
    </h1>
    <form @submit.prevent="signUp">

      <div class="container">
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
          <label  for="password1" class="col-form-label title-init">비밀번호</label>
        </div>
        <div class="col-auto ">
          <input type="password" id="password1" class="form-control" v-model="password1">
        </div>
      </div>

      <div class="row mb-3 g-3 d-flex justify-content-between">
        <div class="col-auto">
          <label  for="password2" class="col-form-label title-init">비밀번호 확인</label>
        </div>
        <div class="col-auto ">
          <input type="password" id="password2" class="form-control" v-model="password2">
        </div>
      </div>

      <div class="row mb-3 g-3 d-flex justify-content-center">
        

        <div class="col-auto">
          <input class="btn btn-primary" type="submit" value="Sign up">
        </div>
      </div>
      </div>
    </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    }
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