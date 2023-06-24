<template>
  <div>
    {{room_id}} 번째 CHAT rOOM
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'ChatRoomView',
    data() {
      return {
        room_id:this.$route.params.roompk,
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
  methods: {
    getChatRoomList(){
      axios({
        method: 'get',
        url: `${API_URL}/accounts/${this.user}/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.followers = res.data.followers
        this.following_cnt = res.data.following_cnt
        this.post_cnt = res.data.post_cnt
        this.image_file = res.data.profile_info.length ? res.data.profile_info[0].image_raw : ''
        this.nickname = res.data.profile_info.length ? res.data.profile_info[0].nickname : ''
        this.introduction = res.data.profile_info.length ? res.data.profile_info[0].introduction : ''
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
    // created(){
    //   this.getChatRoomList()
    // }

}
</script>

<style scoped>

</style>