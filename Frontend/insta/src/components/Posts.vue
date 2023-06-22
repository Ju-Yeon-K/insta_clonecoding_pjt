<template>
  <div>
    <div class="container">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="post in posts" :key="post.pk" class="col-4">
        <Post :image="post.image" :content="post.content" :user="post.user" :like_users="post.like_users" />
      </div>
      <!-- {% for post in posts %}
      
      <div class="col-2 card m-2" style="width: 18rem;">
        <a href="{% url 'posts:detail' post.pk %}">
        {% if post.image %}
        <img src="{{ post.image.url }}" class="card-img-top mt-2 imgsizing">
        {% endif %}
        </a>
        
        <div class="card-body">
            <form action="{% url 'posts:likes' post.pk %}" method="POST">

              <p>
                {% if request.user not in post.like_users.all %}
              <i  class="far fa-heart" style="color: crimson;"></i>
                {% else %}
              <i type="submit" class="fas fa-heart" style="color: crimson;"></i>
              {% endif %}
              {{post.like_users.count}}
              </p>
            </form>
          
          <p class="card-text">{{post.content}}</p>
          <p>posted by : <a href="{% url 'profile' post.user.username%}">{{post.user}}</a>
          <a href="{% url 'posts:detail' post.pk %}" class="btn btn-secondary">detail</a> 
          {% if request.user == post.user %}
          <a href="{% url 'posts:update' post.pk %}">
            <i class="bi bi-scissors"></i>
          </a>
          <a href="{% url 'posts:delete' post.pk %}">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
              <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
            </svg>
          </a>
          {% endif %}
        </div>
      </div>
      
      {% endfor %} -->
    </div>
  </div>
  </div>
</template>

<script>
import Post from './Post.vue'
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
  components:{
    Post
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
    }
  },
  created(){
    this.getPostList()
  }
}
</script>

<style scoped>

</style>