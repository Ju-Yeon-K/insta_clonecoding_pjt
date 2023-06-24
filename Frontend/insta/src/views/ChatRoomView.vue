<template>
  <div>
    <div class="container">
      <div class="row d-flex justify-content-center">
          <div class="col-6">
              <div class="form-group">
                  <!-- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/340px-Default_pfp.svg.png?20220226140232" alt=""/> -->
                  <label for="exampleFormControlTextarea1" class="h4 pt-5">
                      {{room_id}} 번째 CHAT rOOM</label>
                  <textarea v-model="chatLog" class="form-control" id="chat-log" cols="100" rows="20" readonly></textarea><br>
              </div>

              <div class="input-group my-2">
                <input type="text" class="form-control" :placeholder='`${username}으로 메시지 전송...`' aria-describedby="button-addon2" v-model="messageInput" @keyup.enter="sendMessage">
                <button class="btn comment-post align-text-bottom" @click.prevent="sendMessage">  Send  </button>
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
    name:'ChatRoomView',
    data() {
      return {
        room_id:this.$route.params.roompk,

        socket:null,

        messageInput:null,
        chatLog:'',
        messages:[],

        logs:[],
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
    connect() {
        this.socket = new WebSocket(
            `ws://127.0.0.1:8000/ws/chat/${this.room_id}/${this.username}/`
        )
        this.socket.onopen = () => {
          this.logs.push({ type: 'INFO', msg: 'CONNECTED' })
          this.disabled = false
        }
        this.socket.onerror = () => {
          this.logs.push({ type: 'ERROR', msg: 'ERROR:' })
        }
        this.socket.onmessage = ({ data }) => {

          this.chatLog += JSON.parse(data)['message'] + '\n'
          this.logs.push({ type: 'RECV', msg: 'RECV:' + data })
        }
        this.socket.onclose = (msg) => {
          this.logs.push({ type: 'ERROR', msg: 'Closed (Code: ' + msg.code + ', Message: ' + msg.reason + ')' })
        
      }
    },
    sendMessage(){
      this.socket.send(JSON.stringify({
          'message': this.messageInput
      }));
      this.messageInput = null;
    },
    getMessages(){
      axios({
        method: 'get',
        url: `${API_URL}/chat/${this.room_id}/messages/`,
        headers: {
          'Authorization': 'Token ' + this.token
          }
      })
      .then((res) => {
        this.messages = res.data.results
        for(let i=this.messages.length -1 ;i > -1 ;i--){
          this.chatLog = this.messages[i]['content'] + '\n' + this.chatLog
        }
        
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created(){
    this.getMessages()
    this.connect()
  },
  destroyed(){
    this.socket.close()
  },
  }
</script>

<style scoped>

</style>