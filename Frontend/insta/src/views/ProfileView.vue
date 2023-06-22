<template>
  <div>
    <div class="container text-start">
      <div class="row">
        <div class="d-flex justify-content-between" >          
          
          <span v-if="is_me" class="title">{{profile.user}} 님의 프로필</span> <!-- {% if request.user.id == profile.user_id %}   -->
          <span v-else class="title">내 프로필</span>

          <div class="mt-auto mb-0">
          <router-link :to="{ name:'passwordChange' }">
            <button type="submit" class="btn btn-primary mybtn">Change PW</button>
          </router-link>
          <router-link :to="{ name:'delete' }">
            <button type="submit" class="btn btn-danger mybtn">Delete</button>
          </router-link>
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
    
        <div v-if="nickname" class="row ms-2">{{}} </div> 
        <div v-else class="row m-2">No NickName</div>

        <div v-if="introduction" class="row ms-2">{{}}</div>
        <div v-else class="row mx-2">No Introduction</div>

        <div class="row">
          <div class="col-2 mt-2">
            
           <!-- <form action="{% url 'accounts:follow' profile.user.pk %}" method="POST">  {% if request.user != profile.user %}
                <button type="submit" class="btn btn-secondary" style="width: 11rem;">팔로잉</button> {% if request.user in profile.user.followers.all %}
                <button type="submit" class="btn btn-primary" style="width: 11rem;">팔로우</button>
            </form> -->
           
          </div>
        </div>

        <Posts />
        
      </div>
</template>

<script>
import Posts from '@/components/Posts.vue'
export default {
    name:'ProfileView',
    data() {
      return {
        user_pk:this.$route.params.userpk,
        is_me:false,
        image_file:null,
        nickname:null,
        introduction:null,
      }
  },
  components:{
    Posts
  },

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