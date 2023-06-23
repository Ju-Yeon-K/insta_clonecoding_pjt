<template>
  <div>
    <div class="container">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="post in posts" :key="post.pk" class="col-4">
          <div class="card m-2" style="width: 19rem;">
            <router-link :to="{ name:'postDetail', params: {postpk : post.pk} }">
            <img :src="'http://127.0.0.1:8000'+ post.image" class="card-img-top imgsizing">
            </router-link>
                <div class="card-body">
                <router-link :to="{ name:'profile', params: {user : post.user}  }" class="card-text" >{{post.user}}</router-link> 
                <p class="card-text">{{post.content}}</p>

                <p class="card-text">
                  <button type="button" @click.prevent="postLike(post.pk, $event)">
                    <svg v-if="post.like_users.includes(`${username}`)" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#fe2351" class="bi bi-heart-fill" viewBox="0 0 16 16">
                      <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
                    </svg>   
                    <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#fecddb" class="bi bi-heart-fill"  viewBox="0 0 16 16">
                      <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
                    </svg>
                  {{post.like_cnt}}
                  </button>
                </p>

                <div v-if="post.user==username" class="logo d-flex justify-content-end"> <!--여기 설정 -->
                  <router-link :to="{ name:'updatepost', params: { postpk : post.pk} }">✏️Edit</router-link>
                  <a href="#" @click.prevent="deletePost(post.pk, $event)">🗑️Delete</a>
                </div>
                </div> 
          </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'Posts',
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
  height: 20rem;
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
</style>