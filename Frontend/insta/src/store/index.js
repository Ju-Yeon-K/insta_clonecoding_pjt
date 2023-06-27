import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
import axios from 'axios'
Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    username: "AnonymousUser",
    // my_img: null,
  },
  getters: {
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    SAVE_USERNAME(state, username) {
      state.username = username
    },

  },
  actions: {
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SAVE_USERNAME', username)
        router.push({name : 'home'})
      })
      .catch((err) => {
        alert('회원 정보가 없습니다 🥲 (체크 필요)') 
      })
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          "Authorization": "Token " + this.state.token
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', null)
        context.commit('SAVE_USERNAME', "AnonymousUser")
        router.push({name : 'login'})
      })
      .catch((err)=> {
        alert('로그아웃 요청이 올바르지 않습니다 🥲 (체크 필요)')
      })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          context.commit('SAVE_USERNAME', username)
          router.push({name : 'home'})
        })
        .catch((err) => {
          if (err.response.data.username) {
            const message = err.response.data.username[0]
            alert('아이디 :' + message)
          } else if (err.response.data.password1) {
            const message = err.response.data.password1[0]
            alert(message)
          } else if (err.response.data.password2) {
            const message = err.response.data.password2[0]
            alert(message)
          }
      })
    },
    changePassword(context, payload) {
      const old_password = payload.old
      const new_password1 = payload.password1
      const new_password2 = payload.password2

      axios({
        method: 'POST',
        url: `${API_URL}/accounts/password/change/`,
        data: {
          old_password, new_password1, new_password2
        },
        headers: {
          "Authorization": "Token " + this.state.token
        }
      })
        .then((res) => {
          alert('비밀번호가 변경되었습니다.')
          router.push({ name:'profile', params: {user : this.state.username}  })
        })
        .catch((err) => {
          alert('기존 비밀번호를 잘 못 입력하였습니다.') // 추후 밸리데이션 필요함
      })
    },
    userDelete(context) {
      axios({
        method: 'POST',
        url: `${API_URL}/accounts/user/`,

        headers: {
          "Authorization": "Token " + this.state.token
        }
      })
        .then((res) => {
          router.push({ name:'login'})
          context.commit('SAVE_TOKEN', null)
        })
        .catch((err) => {
          console.log(err)
      })
      
    },
  },
  modules: {
  }
})
