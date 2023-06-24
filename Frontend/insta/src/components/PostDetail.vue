<template>
  <div class="d-flex justify-content-center">
    <div class="card m-2" style="width: 60rem;">
      <img :src="'http://127.0.0.1:8000'+ image" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">
          <router-link :to="{ name:'profile', params: { user : user} }" class="card-text" >{{user}}</router-link>
        </h5>
        <p class="card-text">{{content}}</p>

        <div class="card-text d-flex justify-content-between">

            <button type="button" @click.prevent="postLike">
              <svg v-if="is_user_liked" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#fe2351" class="bi bi-heart-fill" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
              </svg>   
              <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#fecddb" class="bi bi-heart-fill"  viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
              </svg>   {{like_cnt}}
            </button>

            <div v-if="user==username" class="logo"> 
              <router-link :to="{ name:'updatepost', params: { postpk : this.post_pk} }">✏️Edit</router-link>
              <a href="#" @click.prevent="deletePost(post.pk, $event)">🗑️Delete</a>
            </div>
        </div>

        <!-- Comments -->
        <div class="card-text mt-3">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chat" viewBox="0 0 16 16">
          <path d="M2.678 11.894a1 1 0 0 1 .287.801 10.97 10.97 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8.06 8.06 0 0 0 8 14c3.996 0 7-2.807 7-6 0-3.192-3.004-6-7-6S1 4.808 1 8c0 1.468.617 2.83 1.678 3.894zm-.493 3.905a21.682 21.682 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a9.68 9.68 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105z"/>
          </svg> {{comments.length}}  <span class="ms-2 text-secondary">댓글 모두 보기</span>

          <div v-for="comment in comments" :key='comment.pk' class="">
            <div class="my-2" style="width:18rem;">
              <router-link :to="{ name:'profile', params: { user : comment.user} }" class="card-text" >{{comment.user}}</router-link>
                <span class="ms-3 text-secondary">{{comment.created_at.slice(14,16)}}분 전</span>
            </div>
            <div>
              {{comment.content}} 
              <button v-if="comment.user==username" @click.prevent="commentDelete(comment.id, $event)">🗑️
              </button>
              <div v-else style="width: 7rem;"></div>
            </div>
          </div> 

        
          <div class="input-group my-2">
            <input type="text" class="form-control" :placeholder='`${username}으로 댓글달기...`' aria-describedby="button-addon2" v-model="comment" @keyup.enter="commentCreate">
            <button class="btn comment-post align-text-bottom" @click.prevent="commentCreate">  게시  </button>
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
  name:'postDetail',
  data(){
    return{
      post_pk:this.$route.params.postpk,

      image:null,
      user:null,
      content:null,
      like_cnt:0,
      comments:[],

      is_user_liked:false,
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
        this.image = res.data.image
        this.user = res.data.user
        this.content = res.data.content
        this.like_cnt = res.data.like_cnt
        this.comments = res.data.comments
        this.is_user_liked = res.data.like_users.includes(this.username)
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
        url: `${API_URL}/posts/${this.post_pk}/likes/`,
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
.comment-post{
  color: rgb(117, 167, 150);
  
}
.comment-post:hover{
  color: rgb(63, 134, 111);
}
.form-control {
  width: 1000rem;
}
</style>