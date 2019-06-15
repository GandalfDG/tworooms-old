import Vue from 'vue'
import Router from 'vue-router'
import LandingPage from '@/components/LandingPage'
import NewGame from '@/components/NewGame'
import Lobby from '@/components/Lobby'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'LandingPage',
      component: LandingPage
    },
    {
      path: '/new/',
      name: 'NewGame',
      component: NewGame
    },
    {
      path: '/lobby/:accessCode',
      name: 'Lobby',
      component: Lobby,
      props: true
    }
  ]
})
