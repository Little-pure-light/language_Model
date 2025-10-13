import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

import router from './router'; // <-- 加這行

const app = createApp(App);
app.use(router); // <-- 加這行
app.mount('#app');
