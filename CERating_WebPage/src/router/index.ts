import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/LoginRegister.vue'
import Error404 from '../views/Error404.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/announcement', /*帮助中心*/
    name: 'Announcement',
    component: () => import('../views/announcement.vue')
  },
  {
    path: '/bulletin', /*公告*/
    name: 'Bulletin',
    component: () => import('../views/bulletin.vue')
  },
  {
    path: '/query', /*查询*/
    name: 'Query',
    component: () => import('../views/query.vue')
  },
  {
    path: '/queryresult', /*查询结果*/
    name: 'QueryResult',
    component: () => import('../views/queryresult.vue')
  },
  {
    path: '/recharge', /*查询*/
    name: 'recharge',
    component: () => import('../views/recharge.vue')
  },
  {
    path: '/:catchAll(.*)',
    name: 'Error404',
    component: Error404
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
