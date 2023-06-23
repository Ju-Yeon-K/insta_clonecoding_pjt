<template>
  <div class="d-flex justify-content-center">
    <div class="card m-2" style="width: 30rem;">
      <img :src="'http://127.0.0.1:8000'+ post_info.image" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">
          <router-link :to="{ name:'profile', params: { user : post_info.user} }" class="card-text" >{{post_info.user_name}}</router-link>
        </h5>
        <p class="card-text">{{post_info.content}}</p>

        <div class="card-text d-flex justify-content-end">

            <button type="button" @click.prevent="postLike">
              <svg v-if="is_user_liked" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#fe2351" class="bi bi-heart-fill" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
              </svg>   
              <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#fecddb" class="bi bi-heart-fill"  viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
              </svg>   {{post_info.like_cnt}}
            </button>
            <div class="col-8"></div>
            <div class="logo"> <!--여기 설정 -->
              <router-link :to="{ name:'updatepost', params: { postpk : this.post_pk} }">✏️Edit</router-link>
              <a href="#" @click.prevent="deletePost(post.pk, $event)">🗑️Delete</a>
            </div>
        </div>

        <p class="card-text mt-3">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-chat-left" viewBox="0 0 16 16">
          <path d="M14 1a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H4.414A2 2 0 0 0 3 11.586l-2 2V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12.793a.5.5 0 0 0 .854.353l2.853-2.853A1 1 0 0 1 4.414 12H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
          </svg> {{comment_cnt}}  Comments

          <div class="input-group mb-3">
          <input type="text" class="form-control" placeholder="New Comment" aria-describedby="button-addon2" v-model="comment" @keyup.enter="commentCreate">
          <button class="btn btn-outline-secondary" type="button" id="button-addon2" @click.prevent="commentCreate">  Post  </button>
        </div>

          <div v-for="comment in post_info.comments" :key='comment.pk' class="d-flex justify-content-between">
            <div style="width:18rem;">
              <router-link :to="{ name:'profile', params: { user : post_info.user} }" class="card-text" >{{comment.user}}</router-link>
               : {{comment.content}} 
            </div>
            <div>
              {{comment.created_at.slice(0,10)}}
              <button @click.prevent="commentDelete(comment.id, $event)">🗑️
              </button>
            </div>
        </div> 
        </p> 
        
      </div>
    </div>


  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'postDetail',
  data(){
    return{
      post_pk:this.$route.params.postpk,
      post_info:null,
      is_user_liked:false,
      comment_cnt:0,
      comment:null,
    }
  },
  computed:{
    token(){
      return this.$store.state.token
    },
    username(){
      return this.$store.state.username
    },
  },
  methods: {
    getPostInfo(){
      axios({
        method: 'get',
        url: `${API_URL}/posts/${this.post_pk}/detail/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.post_info = res.data
        this.is_user_liked = this.post_info.like_users.includes(this.username)
        this.comment_cnt = this.post_info.comments.length
        
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
        this.$router.push({name : 'home'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    postLike(){
      axios({
        method: 'POST',
        url: `${API_URL}/posts/${this.post_info.pk}/likes/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.getPostInfo()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    commentCreate(){
      const comment = this.comment
      axios({
        method: 'POST',
        url: `${API_URL}/posts/${this.post_pk}/comments/create/`,
        headers: {
          'Authorization': 'Token ' + this.token
          },
        data: {
          content:comment
        }
      })
      .then((res) => {
        this.comment = null
        this.getPostInfo()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    commentDelete(comment_pk, event){
      axios({
        method: 'DELETE',
        url: `${API_URL}/posts/${this.post_pk}/comments/${comment_pk}/delete/`,
        headers: {
          'Authorization': 'Token ' + this.token
          },
      })
      .then((res) => {
        this.getPostInfo()
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created(){
    this.getPostInfo()
  },
}
</script>

<style scoped>
*{
  text-decoration: none;
}
a {
  color: black;
}
a:hover{
  cursor: pointer;
  color: rgb(117, 167, 150);
}
</style>