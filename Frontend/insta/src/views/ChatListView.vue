<template>
  <div>
    <b-list-group>

      <!-- 채팅방 목록 -->
      <div v-for="room in rooms" :key="room.room_id">
        <router-link :to="{ name:'chatRoom', params: {roompk : room.room_id} }">
          <b-list-group-item button class="d-flex justify-content-between align-items-center">
            채팅하기
            <b-badge pill variant="primary">Primary</b-badge>
          </b-list-group-item>
        </router-link>
      </div>

    </b-list-group>

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'chatListView',
    data() {
      return {
        rooms:[],
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
        method: 'GET',
        url: `${API_URL}/chat/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.rooms = res.data.results
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
    created(){
      this.getChatRoomList()
    }

}
</script>

<style scoped>

</style>