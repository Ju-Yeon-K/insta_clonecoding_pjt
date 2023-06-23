<template>
  <div>
    <br>
    <br>
    <div class="container">
    <div class="row mx-0 my-0">

      <div v-for="post in posts" :key="post.pk" class="card col-4 mx-0 my-0 px-0 py-0" style="border-radius:0;border:solid 0px">
        
            <router-link :to="{ name:'postDetail', params: {postpk : post.pk} }">
            <img :src="'http://127.0.0.1:8000'+ post.image" class="card-img-top ">
            </router-link>

            <!-- <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#fecddb" class="bi bi-heart-fill"  viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
            </svg>
                {{post.like_cnt}} -->
      </div>


      </div>
    <br><br><br><br><br><br><br><br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'Posts',
  props:{
    user_profile:String
  },
  data(){
    return {
      postUser:this.user_profile,
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
    getUserPostList(){ // 페이지 네이션 추후 하기
      axios({
        method: 'get',
        url: `${API_URL}/posts/${this.postUser}`,
        headers: {
          'Authorization': 'Token ' + this.token
          },
      })
      .then((res) => {
        this.posts = res.data.results
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 여기 아래로 더 봐 

    deletePost(post_pk, event){
      axios({
        method: 'DELETE',
        url: `${API_URL}/posts/${post_pk}/delete/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.getUserPostList()
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
        this.getUserPostList()
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created(){
    this.getUserPostList()
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
img {
  width: 27rem;
  height: 27rem;
  border-radius: 0;
}
img:hover {
  background-color: #000;/* 까만색(0,0,0) */
  opacity:0.5; /* 80% 불투명도 */
}
</style>