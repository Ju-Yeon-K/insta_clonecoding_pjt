<template>
  <div>
    <div class="container text-start">
      <div class="row">
        <div class="d-flex justify-content-between" >          
          
          <span v-if="is_me" class="title">{{profile.user}} 님의 프로필</span> <!-- {% if request.user.id == profile.user_id %}   -->
          <span v-else class="title">내 프로필</span>

          <div class="mt-auto mb-0">
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

          <button @click="logout" type="submit" class="btn btn-secondary mybtn">Log out</button>
        </div>


        </div>
      </div>
    </div>

    <div class="container text-center">
          <div class="row">
            <div class="col-2" >
                <img v-if="image_file" :src="'http://127.0.0.1:8000/media/'+ image_file" class="card-img-top imgbox mt-2"> 
                <img v-else src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/340px-Default_pfp.svg.png?20220226140232" class="card-img-top imgbox mt-2">
            </div>
            <div class="col-4"></div>
            <div class="col-2 mt-4">
              {{}} <br>
              게시물
            </div>
            <div class="col-2 mt-4">
              {{}} <br>
              팔로워
            </div>
            <div class="col-2 mt-4">
              {{}} <br>
              팔로잉
            </div>
          </div>
        </div>
    
        <div v-if="nickname" class="row ms-3">{{}} </div> 
        <div v-else class="row m-2">No NickName</div>

        <div v-if="introduction" class="row ms-3">{{}}</div>
        <div v-else class="row mx-2">No Introduction</div>

        <div class="row">
          <div class="col-2 mt-2">
            
            <button type="button" @click.prevent="follow" v-if="!is_me">  
                <button v-if="!is_following" type="submit" class="btn btn-secondary" style="width: 11rem;">팔로잉</button> 
                <button v-else type="" class="btn btn-primary" style="width: 11rem;">팔로우</button>
            </button> 
           
          </div>
        </div>

        <MyPosts />
        
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
        user_pk:this.$route.params.userpk,
        is_me:false,
        is_following:false,
        image_file:null,
        nickname:null,
        introduction:null,
      }
  },
  components:{
    MyPosts
  },
  methods: {
    follow(){
      
    },
    logout(){
      this.$store.dispatch('logout')
    },
    Delete(){
      console.log('실행중')
      this.$store.dispatch('userDelete')
    }
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
</style>