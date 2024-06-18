import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/Login.vue'
import RegisterUserView from '../components/RegisterUsers.vue'
import MenuView from '../components/Menu.vue'
import PersonaView from "../components/Persona.vue"
import HomeView from "../components/Home.vue"
import InstalacionesView from "../components/Instalaciones.vue"
import EquipamientoView from "../components/Equipamiento.vue"
import MantenimientoView from "../components/Mantenimiento.vue"
import PrestamoView from "../components/Prestamo.vue"
// import FooterView from "../components/footer.vue"

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
      path: '/menu',
      name: 'menu',
      component: MenuView,
      children: [
        { path: '/personas', name: 'personas', component: PersonaView },
        { path: '/home', name: 'Home', component: HomeView },
        { path: '/instalaciones', name: 'instalaciones', component: InstalacionesView },
        { path: '/equipamiento', name: 'equipamiento', component: EquipamientoView },
        { path: '/mantenimiento', name: 'mantenimiento', component: MantenimientoView },
        { path: '/prestamo', name: 'prestamo', component: PrestamoView }

      ]
    }

  ]
})

export default router
