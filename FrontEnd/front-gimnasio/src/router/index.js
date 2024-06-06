import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/Login.vue'
import RegisterUserView from '../components/RegisterUser.vue'
import RegisteUserView from '../components/RegisterUsers.vue'
import MenuView from '../components/Menu.vue'
// import dashboardView from '@views/dashboard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LoginView
    },

    {
      path: '/register',
      name: 'register',
      component: RegisterUserView
    },
    {
      path: '/registe',
      name: 'registe',
      component: RegisteUserView
    },
    {
      path: '/menu',
      name: 'menu',
      component: MenuView,
      children:[
        {path:'/personas', name:'personas', component: RegisteUserView}

      ]
    }
  
  ]
})

export default router
