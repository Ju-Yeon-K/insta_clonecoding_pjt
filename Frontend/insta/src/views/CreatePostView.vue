<template>
<div>
    <h1>New Post</h1>
    <div class="container">
        <div class="row">

            <div class="mb-3">
            <label for="formFile" class="form-label">Photo</label>
            <v-file-input v-model="file" name="files" class="form-control" type="file" id="formFile" />
            <input type="file" class="form-control" id="formFile">
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
    <button type="submit" class="btn btn-primary ms-10" @click="CreatePost">Submit</button>

</div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'CreatePostView',
  data() {
    return {
      content: null,
      image: null,
    }
  },
  computed: {
    token(){
      return this.$store.state.token
    },
  },
  methods: {
    CreatePost() {
      const content = this.content
      const image = this.image
      axios({
        method: 'post',
        url: `${API_URL}/posts/create/`,
        data: {
          content, image
        },
        headers: {
          "Authorization": "Token " + this.token
        }
      })
        .then((res) => {
          this.$router.push({name : 'profile'})
        })
        .catch((err) => {
            console.log(err)
      })
    },
  }
}
</script>

<style>

</style>