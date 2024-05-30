import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/Login.vue'
import RegisterUserView from '../components/RegisterUser.vue'
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
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/dynamic',
      name: 'dynamic',
      component: Dynamic
    },

  ]
})

export default router
