import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import CreatePostView from '../views/CreatePostView.vue'
import ProfileView from '../views/ProfileView.vue'

Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/newpost',
    name: 'createpost',
    component: CreatePostView,
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

import store from '@/store'
router.beforeEach((to, from, next)=>{
  const isLoggedIn = store.state.token ? true : false
  const allowPages = ['login', 'signup']
  const isAuthRequired = !allowPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    next({name:'login'})
  } else {
    next()
  }

})

export default router
