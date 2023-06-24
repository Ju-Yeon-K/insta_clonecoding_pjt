<template>
  <div>
    <div class="container">
    <div class="row g-4 d-flex justify-content-center">
      <div v-for="post in posts" :key="post.pk" lass="m-2 col-12" style="width: 60rem;border:solid black 1px;">
          <!-- <div class="card m-2 col-12" style="width: 20rem;"> -->
            
            <router-link :to="{ name:'profile', params: {user : post.user}  }" class="card-text" >{{post.user}}</router-link> 
            
            <router-link :to="{ name:'postDetail', params: {postpk : post.pk} }">
            <img :src="'http://127.0.0.1:8000'+ post.image" class="imgsizing">
            </router-link>

                <p>{{post.content}}</p>

                  <button type="button" @click.prevent="postLike(post.pk, $event)">
                    <svg v-if="post.like_users.includes(`${username}`)" xmlns="http://www.w3.org/2000/svg" width="22" height="22"  fill="#fe2351" class="bi bi-heart-fill" viewBox="0 0 16 16">
                      <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
                    </svg>   
                    <svg v-else xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="#fecddb" class="bi bi-heart-fill"  viewBox="0 0 16 16">
                      <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
                    </svg>
                  {{post.like_cnt}}
                  </button>


                <div v-if="post.user==username" class="logo d-flex justify-content-end"> <!--여기 설정 -->
                  <router-link :to="{ name:'updatepost', params: { postpk : post.pk} }">✏️Edit</router-link>
                  <a href="#" @click.prevent="deletePost(post.pk, $event)">🗑️Delete</a>
                </div>
                </div> 

      <!-- </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'Home',
  data(){
    return {
      posts: [],
    }
  },
  computed: {
    token(){
      return this.$store.state.token
    },
    username(){
      return this.$store.state.username
    },
  },
  methods:{
    getPostList(){ // 페이지 네이션 추후 하기
      axios({
        method: 'get',
        url: `${API_URL}/posts/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.posts = res.data.results
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deletePost(post_pk, event){
      axios({
        method: 'DELETE',
        url: `${API_URL}/posts/${post_pk}/delete/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.getPostList()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    postLike(post_pk, event){
      axios({
        method: 'POST',
        url: `${API_URL}/posts/${post_pk}/likes/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.getPostList()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout(){
      this.$store.dispatch('logout')
    }
  },
  created(){
    this.getPostList()
  },

}
</script>

<style scoped>
*{
  text-decoration: none;
}
.imgsizing {
  width: 100%;
  height: 60rem;
}
.card {
  height: 31rem;
}
a {
  color: black;
}
a:hover{
  cursor: pointer;
  color: rgb(117, 167, 150);
}
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
img:hover {
  background-color: #000;
  opacity:0.9;
}
</style>