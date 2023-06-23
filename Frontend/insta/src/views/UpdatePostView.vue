<template>
<div>
    <h1>Update Post</h1>
    <div class="container">
        <div class="row">

            <div class="mb-3">
            <label for="formFile" class="form-label">Photo</label>
            <v-file-input v-model="file" name="files" class="form-control" type="file" id="formFile"></v-file-input> 
            </div>

        </div>
        <div class="col-auto">
          <label  for="content" class="col-form-label">Content</label>
        </div>
        <div class="col-auto">
          <input type="text" id="content" class="form-control" v-model="content">
        </div>
    </div>  
    <br>
    <button type="submit" class="btn btn-primary ms-10" @click="UpdatePost">Submit</button>

</div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'UpdatePostView',
  data() {
    return {
      post_pk:this.$route.params.postpk,
      content: null,
      file: [],
    }
  },
  computed: {
    token(){
      return this.$store.state.token
    },
  },
  methods:{
    getPostInfo(){
      axios({
        method: 'get',
        url: `${API_URL}/posts/${this.post_pk}/detail/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.content = res.data.content
        this.file = res.data.image // 이거 디폴트 값 되게 하기
      })
      .catch((err) => {
        console.log(err)
      })
    },
    UpdatePost() {
      const info = new FormData()
      info.append('image', this.file)
      info.append('content', this.content)
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data', 
          'Authorization': `Token ${this.token}`
          }
      }

      axios({
        method: 'PUT',
        url: `${API_URL}/posts/${this.post_pk}/update/`,
        data: info,
        headers: {
          'Content-Type': 'multipart/form-data', 
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.$router.push({name : 'postDetail', params: { postpk : this.post_pk} })
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created(){
    this.getPostInfo()
  }
}
</script>

<style>

</style>