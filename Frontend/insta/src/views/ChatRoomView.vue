<template>
  <div>
    <div class="chat">
      <div class="chat__header">
        <span class="chat__header__greetings">
          안녕하세요. {{ username }}님!
        </span>
      </div>
       <div class="chat__body" id="chat__body">
          <div v-for="msg in msgs" :key="msg.pk">
              <div
                v-if="msg.user_id == username"
                class="chat__mymessage"
              >
                <!-- :class="[msg.user_id != username ? '' : 'chat__first']"  -->

                <span class="badge_date">{{msg.created_at.slice(0,10)}}</span>
                <span v-if="msg.is_read" class="badge rounded-pill text-bg-light">1</span>
                <p class="chat__mymessage__paragraph">{{ msg.content }}</p>
              </div>

              <div
                v-else
                class="chat__yourmessage"
              >
                <!-- :class="[msg.user_id == username ? '' : 'chat__first']"  -->
              
                <div class="chat__yourmessage__avartar">
                  <img
                    :src="'http://127.0.0.1:8000/media/'+ userImg"
                    class="chat__yourmessage__img"
                    v-if="userImg"
                  />
                  <img
                    :src="avatar"
                    class="chat__yourmessage__img"
                    v-else
                  />

                </div>
                <div>
                  <p class="chat__yourmessage__user" v-if="!isSame"> 
                    {{ msg.user_id }}
                  </p>
                  <div class="chat__yourmessage__p">
                    <p class="chat__yourmessage__paragraph">
                      {{ msg.content }}
                    </p>

                  </div>
                </div>
              </div>
            </div>
      </div> 

      <div class="form">
    <input
      class="form__input"
      type="text"
      :placeholder='`${username}으로 메시지 전송...`'
      v-model="messageInput"
      @keyup.enter="sendMessage"
    />
    <div @click="sendMessage" class="form__submit">
      <svg
        width="30"
        height="30"
        viewBox="0 0 68 68"
        fill="#CCCCCC"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g clip-path="url(#clip0_26_10)">
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M48.0833 19.799C48.619 20.3347 48.806 21.127 48.5665 21.8457L35.8385 60.0294C35.5946 60.7614 34.9513 61.2877 34.1855 61.382C33.4198 61.4763 32.6681 61.1217 32.2539 60.4707L22.593 45.2893L7.41158 35.6285C6.76065 35.2142 6.40604 34.4625 6.50031 33.6968C6.59458 32.931 7.12092 32.2878 7.85287 32.0438L46.0366 19.3159C46.7553 19.0763 47.5476 19.2633 48.0833 19.799ZM26.5903 44.1204L33.3726 54.7782L42.0926 28.6181L26.5903 44.1204ZM39.2642 25.7897L23.7619 41.292L13.1041 34.5097L39.2642 25.7897Z"
            fill=""
          />
        </g>
        <defs>
          <clipPath id="clip0_26_10">
            <rect
              width="48"
              height="48"
              fill="white"
              transform="translate(33.9412) rotate(45)"
            />
          </clipPath>
        </defs>
      </svg>
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
        userImg:this.$route.query.img_raw,

        socket:null,

        messageInput:null,
        chatLog:'',
        msgs:[],

        logs:[],

        isSame: false,
        avatar: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/340px-Default_pfp.svg.png?20220226140232"
      }
  },
  computed: {
    token(){
      return this.$store.state.token
    },
    username(){
      return this.$store.state.username
    },
    touserimg(){
      return this.$store.state.user_img_saver
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
          console.log(JSON.parse(data))
          this.msgs.push(JSON.parse(data))
          this.logs.push({ type: 'RECV', msg: 'RECV:' + data })
        }
        this.socket.onclose = (msg) => {
          this.logs.push({ type: 'ERROR', msg: 'Closed (Code: ' + msg.code + ', Message: ' + msg.reason + ')' })
        
      }
    },
    sendMessage(){
      this.socket.send(JSON.stringify({ 
          'content': this.messageInput
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
        this.msgs = res.data.results.reverse()
        // for(let i=this.messages.length -1 ;i > -1 ;i--){
        //   this.chatLog = this.messages[i]['content'] + '\n' + this.chatLog
        // }
        
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // isSamePerson(msg, prev) {
    //   if (prev === null) {
    //     return false;
    //   } else if (prev[0]?.from.name == msg?.from.name) {
    //     return true;
    //   } else {
    //     return false;
    //   }
    // },
  },
  created(){
    this.getMessages()
    this.connect()
    // this.isSame = this.isSamePerson(this.msg, this.prev);
    // if (this.msg?.from.avatar) {
    //   this.avatar = this.msg?.from.avatar
    // }
  },
  destroyed(){
    this.socket.close()
  },
  }
</script>

<style scoped>
.chat {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.chat__header {
  background: #ffffff;
  box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.05);
  border-radius: 24px 24px 0px 0px;
  padding: 1.8rem;
  font-size: 16px;
  font-weight: 700;
}

.chat__header__greetings {
  color: #292929;
}
.chat__body {
  padding: 2rem;
  overflow: scroll;
  scroll-behavior: smooth;
}

.chat__body::-webkit-scrollbar {
  display: none;
}
.form {
  display: flex;
  justify-content: space-between;
  padding: 0.3rem;
  margin-bottom: 1rem;
  background: #ffffff;
  border-radius: 15px 15px 24px 24px;
  box-shadow: 0px -5px 30px rgba(0, 0, 0, 0.05);
}

.form__input {
  border: none;
  padding: 0.5rem;
  font-size: 16px;
  width: calc(100% - 60px);
}

.form__input:focus {
  outline: none;
}

.form__submit {
  display: flex;
  align-items: center;
  cursor: pointer;
}

svg {
  transition: 0.3s;
}

svg:hover {
  fill: #999999;
}
.chat__mymessage {
  display: flex;
  justify-content: right;
  align-items: flex-end;
  margin: 0;
  min-height: 40px;
  line-break: anywhere;
}

.chat__mymessage__paragraph {
  margin: 0.4rem 0 0 1rem;
  border-radius: 20px 20px 0px 20px;
  max-width: 180px;
  background-color: #efcdbb;
  color: #ffffff;
  padding: 0.8rem;
  font-size: 14px;
}

.chat__first {
  margin-top: 2rem;
}

.chat__yourmessage {
  display: flex;
}

.chat__yourmessage__avartar {
  width: 40px;
  margin-right: 1rem;
}

.chat__yourmessage__img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.chat__yourmessage__user {
  font-size: 14px;
  font-weight: 700;
  color: #292929;
  margin-top: 0;
  margin-block-end: 0rem;
}

.chat__yourmessage__p {
  display: flex;
  align-items: flex-end;
  line-break: anywhere;
}

.chat__yourmessage__paragraph {
  margin: 0.4rem 1rem 0 0;
  border-radius: 0px 20px 20px 20px;
  background-color: #f3f3f3;
  max-width: 180px;
  color: #414141;
  padding: 0.8rem;
  font-size: 14px;
}

.chat__yourmessage__time {
  margin: 0;
  font-size: 12px;
  color: #9c9c9c;
}
.badge_date {
  font-size: 0.5rem;
  color: #595959;

}
</style>