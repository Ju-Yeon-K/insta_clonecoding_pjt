<template>
  <div>
    <b-list-group>
      <!-- 채팅방 목록 -->
      <div v-for="room in rooms" :key="room.room_id">
        <!-- room.user (딕셔너리) 형태 전달해야함. -->
        <router-link :to="{ name:'chatRoom', params: {roompk : room.room_id}, query: { img_raw: room.user.image_raw} }"> 
          <b-list-group-item button class="d-flex align-items-center justify-content-between">
            <div class="d-flex justify-content-start">
              <img v-if="room.user.image_raw" :src="'http://127.0.0.1:8000/media/'+ room.user.image_raw" class="imgbox mt-2"> 
              <img v-else src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/340px-Default_pfp.svg.png?20220226140232" class="card-img-top imgbox mt-2">
              <div class="ms-3">
                {{room.user.user_id}}
                <br>
                <div class="text-secondary">
                  {{room.last_message.content}}
                </div>
                <div class="text-secondary">
                  {{room.last_message.created_at.slice(0,10)}}
                </div>
              </div>
            </div>
            <div class="d-flex justify-content-end">
              <span v-if="room.message_unread_cnt" class="badge rounded-pill text-bg-primary align-self-center">{{room.message_unread_cnt}}</span>
            </div>
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
*{
  text-decoration: none;
  color: black;
}
.imgbox {
  width: 50px;
  height: 50px;
  border-radius: 100%;
  border:3px solid rgb(168, 160, 160);
}
.space{
  width: 40vw;
}
</style>