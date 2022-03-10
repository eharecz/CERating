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
    path: '/consultoverview', /*咨询预览页*/
    name: 'ConsultOverview',
    component: () => import('../views/ConsultOverview.vue')
  },
  {
    path: '/consultdetail', /*咨询详情页*/
    name: 'ConsultDetail',
    component: () => import('../views/ConsultDetail.vue')
  },
  {
    path: '/bulletin', /*公告*/
    name: 'Bulletin',
    component: () => import('../views/bulletin.vue')
  },
  {
    path: '/simurateoverview', /*模拟评级预览页*/
    name: 'Simulate Rating Overview',
    component: () => import('../views/simurateoverview.vue')
  },
  {
    path: '/simurateguide', /*模拟评级导航页*/
    name: 'Simulate Rating Guide',
    component: () => import('../views/simurateguide.vue')
  },
  {
    path: '/simurate', /*模拟评级*/
    name: 'Simulate Rating',
    component: () => import('../views/simurate.vue')
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

router.beforeEach((to,from,next)=>{//beforeEach是router的钩子函数，在进入路由前执行
    if(to.name){//判断是否有标题
        document.title = to.name.toString()
    }
    next()  //执行进入路由，如果不写就不会进入目标页
})

export default router
