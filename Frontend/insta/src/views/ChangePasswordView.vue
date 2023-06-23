<template>
  <div class="userDetail">
    <h1>비밀번호 변경</h1>
      <div class="init_inner">
        <h3>비밀번호를 주기적으로 바꾸면 개인정보 보안에 도움이 됩니다 👍</h3>
      <div class="labeldiv">
        <label  for="old" class="text_basic">기존 비밀번호</label>
      </div>
      <div>
        <input type="password" id="old" class="input_basic" v-model="old">
      </div>
      <div class="labeldiv">
        <label  for="password1" class="text_basic">새 비밀번호</label>
      </div>
      <div>
        <input type="password" id="password1" class="input_basic" v-model="password1">
      </div>
      <div class="labeldiv">
        <label  for="password2" class="text_basic">비밀번호 확인</label>
      </div>
      <div class="">
        <input type="password" id="password2" class="input_basic alert" v-model="password2" @input="validation" @keyup.enter="changePassword">
      </div>
      <div>
        {{alertmsg}}
      </div>

      <div class="">
      </div>
      <div class="">
        <button class="btn" @click="changePassword">비밀번호 변경</button>
      </div>    
    </div>
  </div>
</template>

<script>

export default {
  name: 'ChangePasswordView',
  methods: {
    changePassword() {
      if (!this.old) {
        alert('기존 비밀번호를 입력해주세요')
      } else if (!this.password1) {
        alert('새로운 비밀번호를 입력해주세요')
      } else if (!this.password2) {
        alert('비밀번호 확인을 해주세요.')
      } else {
        const old = this.old
        const password1 = this.password1
        const password2 = this.password2
  
        const payload = {
          old, password1, password2
        }
        this.$store.dispatch('changePassword', payload)
      }
    },
    
    validation() {
      if (this.password2) {
        if (this.password1 != this.password2){
          this.alertmsg = '비밀번호가 일치하지 않아요 🤫'
        } else {
          this.alertmsg = '비밀번호가 일치합니다 😍'
        }
      } else {
        this.alertmsg = ''
      }
    },
  },
  data () {
  return {
    old: null,
    password1: null,
    password2: null,
    alertmsg:null
  }},


}
</script>

<style scoped>
.btn {
  width: 10rem;
  height: 2.5rem;
  margin: 0.5rem;
  background-color: rgb(13, 13, 32);
  color:white;
  border: solid 0px rgb(161, 127, 133);
}
.btn:hover {
  color: rgb(20, 148, 146);
  background-color: rgb(41, 41, 55);
}

.labeldiv {
  margin-bottom: 5px;
}

label {
  font-weight: 500;
}
input {
  margin-bottom: 20px;
  width: 325px;
  height: 40px;
  background-color: rgb(238, 238, 238);
  border : none;
  border-radius: 10px;
  padding-left: 15px;
  font-size: 20px ;
}
</style>
