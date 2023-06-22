<template>
  <div>
    여기는 포스트 디테일 댓글까지 나오게 하는거
    {{post_info}}

<!-- {% if post.image %}
<div class = "boxing m-3">
  <img src="{{ post.image.url }}" class="card-img-top mt-2 ">
</div>
{% endif %}
<div>

  {{post.content}}  <br> 


  {% if request.user == post.user %}
<a href="{% url 'posts:update' post.pk%}" class ="btn btn-outline-secondary btn-sm" >EDIT</a>
<a href="{% url 'posts:delete' post.pk%}" class ="btn btn-outline-secondary btn-sm" >DELETE</a>


{% endif %}
  <hr>
</div>
<span><i class="bi bi-arrow-through-heart-fill">
  <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-through-heart-fill" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M2.854 15.854A.5.5 0 0 1 2 15.5V14H.5a.5.5 0 0 1-.354-.854l1.5-1.5A.5.5 0 0 1 2 11.5h1.793l3.103-3.104a.5.5 0 1 1 .708.708L4.5 12.207V14a.5.5 0 0 1-.146.354l-1.5 1.5ZM16 3.5a.5.5 0 0 1-.854.354L14 2.707l-1.006 1.006c.236.248.44.531.6.845.562 1.096.585 2.517-.213 4.092-.793 1.563-2.395 3.288-5.105 5.08L8 13.912l-.276-.182A23.825 23.825 0 0 1 5.8 12.323L8.31 9.81a1.5 1.5 0 0 0-2.122-2.122L3.657 10.22a8.827 8.827 0 0 1-1.039-1.57c-.798-1.576-.775-2.997-.213-4.093C3.426 2.565 6.18 1.809 8 3.233c1.25-.98 2.944-.928 4.212-.152L13.292 2 12.147.854A.5.5 0 0 1 12.5 0h3a.5.5 0 0 1 .5.5v3Z"/>
  </svg>
</i> {{post.like_users.count}} 개</span>
<div class="m-2"></div>
<form action="{% url 'posts:likes' post.pk %}" method="POST">
  {% csrf_token %}
  {% if request.user in post.like_users.all %}
    <button type="submit" class="btn btn-danger"><span class="bi bi-heart"></span> 좋아요
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-through-heart" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M2.854 15.854A.5.5 0 0 1 2 15.5V14H.5a.5.5 0 0 1-.354-.854l1.5-1.5A.5.5 0 0 1 2 11.5h1.793l.53-.53c-.771-.802-1.328-1.58-1.704-2.32-.798-1.575-.775-2.996-.213-4.092C3.426 2.565 6.18 1.809 8 3.233c1.25-.98 2.944-.928 4.212-.152L13.292 2 12.147.854A.5.5 0 0 1 12.5 0h3a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.854.354L14 2.707l-1.006 1.006c.236.248.44.531.6.845.562 1.096.585 2.517-.213 4.092-.793 1.563-2.395 3.288-5.105 5.08L8 13.912l-.276-.182a21.86 21.86 0 0 1-2.685-2.062l-.539.54V14a.5.5 0 0 1-.146.354l-1.5 1.5Zm2.893-4.894A20.419 20.419 0 0 0 8 12.71c2.456-1.666 3.827-3.207 4.489-4.512.679-1.34.607-2.42.215-3.185-.817-1.595-3.087-2.054-4.346-.761L8 4.62l-.358-.368c-1.259-1.293-3.53-.834-4.346.761-.392.766-.464 1.845.215 3.185.323.636.815 1.33 1.519 2.065l1.866-1.867a.5.5 0 1 1 .708.708L5.747 10.96Z"/>
      </svg></button>
  {% else %}
  <button type="submit" class="btn btn-outline-danger"><span class="bi bi-heart"></span> 좋아요
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-through-heart" viewBox="0 0 16 16">
      <path fill-rule="evenodd" d="M2.854 15.854A.5.5 0 0 1 2 15.5V14H.5a.5.5 0 0 1-.354-.854l1.5-1.5A.5.5 0 0 1 2 11.5h1.793l.53-.53c-.771-.802-1.328-1.58-1.704-2.32-.798-1.575-.775-2.996-.213-4.092C3.426 2.565 6.18 1.809 8 3.233c1.25-.98 2.944-.928 4.212-.152L13.292 2 12.147.854A.5.5 0 0 1 12.5 0h3a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.854.354L14 2.707l-1.006 1.006c.236.248.44.531.6.845.562 1.096.585 2.517-.213 4.092-.793 1.563-2.395 3.288-5.105 5.08L8 13.912l-.276-.182a21.86 21.86 0 0 1-2.685-2.062l-.539.54V14a.5.5 0 0 1-.146.354l-1.5 1.5Zm2.893-4.894A20.419 20.419 0 0 0 8 12.71c2.456-1.666 3.827-3.207 4.489-4.512.679-1.34.607-2.42.215-3.185-.817-1.595-3.087-2.054-4.346-.761L8 4.62l-.358-.368c-1.259-1.293-3.53-.834-4.346.761-.392.766-.464 1.845.215 3.185.323.636.815 1.33 1.519 2.065l1.866-1.867a.5.5 0 1 1 .708.708L5.747 10.96Z"/>
    </svg></button>
  {% endif %}
</form>
<br>

<hr>
  <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-chat-left" viewBox="0 0 16 16">
    <path d="M14 1a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H4.414A2 2 0 0 0 3 11.586l-2 2V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12.793a.5.5 0 0 0 .854.353l2.853-2.853A1 1 0 0 1 4.414 12H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
  </svg>
{% if comments %}
{{comments|length}} comments
{% endif %} 

<hr>
<ul>
  {% for comment in comments %}
<div class = "m-2">
  <li>    
    <form action="{% url 'posts:comments_delete' post.pk comment.pk %}" method='POST'>
      {{comment.user}} <br> {{comment.content}}
      {% if request.user == comment.user %}
      {% csrf_token %}
      <input type="submit" class="btn-close btn-sm" aria-label="Close" value ="  ">
    {% endif %}
     </form>
  </li>

</div>

  {%empty%}
  <p>댓글이 업성요..ㅜㅜ </p>
  {% endfor %}
</ul>


{% if request.user.is_authenticated %}
  <form action="{% url 'posts:comments_create' post.pk %}"method = 'POST'>
    {% csrf_token %}
    

    
    <div class="input-group mb-3">
      {{comment_form.content}}<div class="input-group-append">
        <button type="submit" class="btn btn-outline-secondary" type="button">댓글달기</button>
      </div>
    </div>

  </form>

{% else %}
  <a href="{% url 'accounts:login' %}">댓글 달고싶다면 로그인하시요.</a>
{% endif %} -->
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
      post_info:null
    }
  },
  computed:{
    token(){
      return this.$store.state.token
    }
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
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created(){
    this.getPostInfo()
  }
}
</script>

<style>

</style>