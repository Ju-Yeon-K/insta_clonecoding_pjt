<template>
  <div class="card h-100">
     <img :src="imageURL" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{content}}</h5>
        <p class="card-text">{{user}}</p>
        <p class="card-text">{{like_users}}</p>
      </div>
      <div class="card-footer">
        <small class="text-body-secondary">Last updated 3 mins ago</small>
      </div>   
    
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000'
export default {
  name:'Post',
  data(){
    return{
      imageURL:`//${API_URL}/${this.image}`
    }
  },
  props: {
    image: String,
    content: String,
    user: Number,
    like_users: Number,
  },
  methods: {
    getImgUrl(){

    }
  }
}
</script>

<style scoped>

</style>