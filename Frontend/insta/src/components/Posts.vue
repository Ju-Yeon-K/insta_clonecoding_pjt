<template>
  <div>
    <div class="container">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="post in posts" :key="post.pk" class="col-4">
          <div class="card m-2" style="width: 19rem;">
            <router-link :to="{ name:'postDetail', params: {postpk : post.pk} }">
            <img :src="'http://127.0.0.1:8000/media/'+ post.image" class="card-img-top imgsizing">
            </router-link>
                <div class="card-body">
                <p class="card-text">{{post.content}}</p>
                <span>
                  posted by : 
                </span>
                <router-link :to="{ name:'profile', params: {userpk : post.user}  }" class="card-text" >{{post.user}}</router-link> 

                <!--여기 누르면 action="{% url 'posts:likes' post.pk %}" method="POST" -->
                <i class="far fa-heart" style="color: crimson;"></i> <!--if request.user not in post.like_users.all-->
                <i type="submit" class="fas fa-heart" style="color: crimson;"></i> <!--if request.user not in post.like_users.all-->
                <p class="card-text">{{post.like_users}}</p>

                <div class="logo d-flex justify-content-end"> <!--여기 설정 -->
                  <router-link :to="{ name:'postUpdate' }">✏️Edit</router-link>
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
    }
  },
  methods:{
    getPostList(){
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