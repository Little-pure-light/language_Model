import { createRouter, createWebHistory } from 'vue-router';
import ChatInterface from '../components/ChatInterface.vue';
import StatusPage from '../components/StatusPage.vue'; // ✅ 加入這行

const routes = [
  { path: '/', component: ChatInterface },
  { path: '/status', component: StatusPage }, // ✅ 加入這行
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
