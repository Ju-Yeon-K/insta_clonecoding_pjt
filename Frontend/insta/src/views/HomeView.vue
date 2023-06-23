<template>
  <div>
    <div v-if="token" class="d-flex justify-content-between">
      <div class="mt-auto mb-auto">
        <h2>Hello!</h2>
        <span>
          {{username}}님, 여기는 긴쥬의 소셜네트워크에요 ❤️💞💓💝💘
        </span>
      </div>
      <div class="mt-auto mb-0">
        <router-link :to="{ name:'profile', params: {userpk : this.my_user_pk}  }">
          <button type="submit" class="btn btn-warning">My Profile</button>
        </router-link>
        <!-- <router-link :to="{ name:'changepw' }">
          <button type="submit" class="btn btn-primary">Change PW</button>
        </router-link> -->
          

        <button @click="logout" type="submit" class="btn btn-secondary">Log out</button>
      </div>
    </div>
    <hr>
    <Posts />
</div>
</template>

<script>
import Posts from '@/components/Posts.vue'

export default {
  name: 'Home',
  components:{
    Posts
  },
  computed: {
  token(){
    return this.$store.state.token
  },
  username(){
    return this.$store.state.username
  },
  my_user_pk(){
    return this.$store.state.my_pk
  }},
  methods: {
    logout(){
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style scoped>
.btn {
  width: 7rem;
  height: 2.5rem;
  background-color: #fff;
  color: rgb(133, 187, 186);
  border: none;
}
.btn:hover {
  color: rgb(16, 52, 82);
  background-color: #fff;
}
</style>