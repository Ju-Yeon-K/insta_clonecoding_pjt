<template>
  <div>
    
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
  },
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