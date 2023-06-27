<template>
  <div>
    <div class="container text-start">
      <div class="row">
        <div class="d-flex justify-content-end" >          
          
          <!-- <span v-if="username!=user" class="title">{{user}} 님의 프로필</span> 
          <span v-else class="title">내 프로필</span> -->
          <div v-if="username==user" class="mt-auto mb-0">
          <router-link :to="{ name:'changepw' }">
            <button type="submit" class="btn btn-primary mybtn">Change PW</button>
          </router-link>

          <b-button @click="$bvModal.show('modal-scoped')" class="btn mybtn btn-primary" >Delete</b-button>
              <b-modal id="modal-scoped">
                <template #modal-header="">
                  <!-- Emulate built in modal header close button action -->
                  <h5>회원 탈퇴</h5>
                </template>
                  <p>탈퇴하면 회원 정보를 복구할 수 없습니다.</p>
                  <p>정말로 탈퇴하시겠습니까?</p>
                <template #modal-footer="{ Delete, cancel }">
                  <!-- Emulate built in modal footer ok and cancel button actions -->
                  <b-button size="sm" variant="success" @click="Delete">
                    탈퇴할래요
                  </b-button>
                  <b-button size="sm" variant="danger" @click="cancel()">
                    취소
                  </b-button>
                </template>
              </b-modal>
        </div>


        </div>
      </div>
    </div>

    <div class="container text-center">
      <div class="row align-middle">
        <div class="col-2" >
            <img v-if="image_file" :src="'http://127.0.0.1:8000/media/'+ image_file" class="card-img-top imgbox mt-2"> 
            <img v-else src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/340px-Default_pfp.svg.png?20220226140232" class="card-img-top imgbox mt-2">
        </div>
        <div class="col-4"></div>
        <div class="col-2 my-auto">
          {{post_cnt}} <br>게시물

        </div>
        <div class="col-2 my-auto">
          {{followers.length}} <br>
          팔로워
        </div>
        <div class="col-2 my-auto">
          {{following_cnt}} <br>
          팔로잉
        </div>
      </div>
    </div>
    
    <div class="container text-center">
      <div class="row align-middle">
        <div class="col-2" >
            <p v-if="nickname" class="my-2">{{nickname}} </p> 
            <p v-else class="my-2">NickName</p>

            <p v-if="introduction" class="my-2">{{introduction}}</p>
            <p v-else class="my-2">Introduction</p>
        </div>
        <div class="col-4"></div>

      </div>
    </div>
    
    <div class="container text-center">
      <div class="row align-middle">
    
    <div v-if="user==username">
      <div class="row">
          <div class="col-2 mt-2">
      <b-button @click="$bvModal.show('modal-scoped2')" class="btn btn-secondary" style="width: 11rem;">수정하기</b-button>
          </div></div>

        <b-modal id="modal-scoped2">
          <template #modal-header="">
            <h1>프로필 수정</h1>
          </template>

          <div class="container">
            <div class="row">
              <div class="mb-3">
                <label for="image_file_input" class="form-label">Profile</label>
                <v-file-input v-model="image_file_input" name="files" class="form-control" type="file" id="formFile"></v-file-input> 
              </div>
            </div>

            <div class="col-auto">
              <label  for="Nickname" class="col-form-label">Nickname</label>
            </div>
            <div class="col-auto">
              <input type="text" id="Nickname" class="form-control" v-model="nickname_input">
            </div>        

            <div class="col-auto">
              <label  for="Introduction" class="col-form-label">Introduction</label>
            </div>
            <div class="col-auto">
              <input type="text" id="Introduction" class="form-control" v-model="introduction_input">
            </div>
          </div>
            <br>
          <template #modal-footer="">
            <!-- Emulate built in modal footer ok and cancel button actions -->
            <b-button size="sm" variant="success" @click="UpdateProfile">
              프로필 수정
            </b-button>
            <b-button size="sm" variant="danger" @click="$bvModal.hide('modal-scoped2')">
              취소
            </b-button>
          </template>
        </b-modal>
    </div>
    <div v-else>
        <div class="row">
          <div class="col-2 mt-2">
            <button type="button" @click.prevent="follow">  
                <button v-if="followers.includes(`${username}`)" type="submit" class="btn btn-secondary" style="width: 11rem;">팔로잉</button> 
                <button v-else type="" class="btn btn-primary" style="width: 11rem;">팔로우</button>
            </button>
          </div>
        </div>
    </div>
    </div>
</div>
    

    <MyPosts :user_profile="this.user"/>
        
  </div>
</template>

<script>
import MyPosts from '@/components/MyPosts.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'ProfileView',
    data() {
      return {
        user:this.$route.params.user,

        image_file_input:null,
        nickname_input:null,
        introduction_input:null,

        post_cnt:0,
        following_cnt:0,
        followers:[],
        image_file:null,
        nickname:null,
        introduction:null,
      }
  },
  components:{
    MyPosts
  },
  computed: {
    token(){
      return this.$store.state.token
    },
    username(){
      return this.$store.state.username
    },
  },
  methods: {
    getUserProfileInfo(){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/detail/${this.user}/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.followers = res.data.followers
        this.following_cnt = res.data.following_cnt
        this.post_cnt = res.data.post_cnt
        this.image_file = res.data.profile_info.length ? res.data.profile_info[0].image_raw : ''
        this.nickname = res.data.profile_info.length ? res.data.profile_info[0].nickname : ''
        this.introduction = res.data.profile_info.length ? res.data.profile_info[0].introduction : ''
      })
      .catch((err) => {
        console.log(err)
      })
    },
    follow(){
      axios({
        method: 'POST',
        url: `${API_URL}/accounts/follow/${this.user}/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.getUserProfileInfo()

      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout(){
      this.$store.dispatch('logout')
    },
    Delete(){
      this.$store.dispatch('userDelete')
    },
    UpdateProfile(){
      const info = new FormData()
      info.append('image_raw', this.image_file_input)
      info.append('nickname', this.nickname_input)
      info.append('introduction', this.introduction_input)

      axios({
        method: 'post',
        url: `${API_URL}/accounts/profile/update/`,
        data: info,
        headers: {
          'Content-Type': 'multipart/form-data', 
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.$bvModal.hide('modal-scoped2')
        this.getUserProfileInfo()
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
    created(){
      this.getUserProfileInfo()
    }

}
</script>

<style scoped>
.mybtn {
  width: 7rem;
  height: 2.5rem;
  background-color: #fff;
  color: rgb(133, 187, 186);
  border: none;
}
.mybtn:hover {
  color: rgb(16, 52, 82);
  background-color: #fff;
}
.title{
  font-size: 2rem;
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
  width: 200px;
  height: 200px;
  border-radius: 100%;
  border:3px solid rgb(168, 160, 160);
}
.imgsizing {
  height: 270px;
}
</style>