// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import ChatInterface from '../components/ChatInterface.vue';
import StatusPage from '../components/StatusPage.vue';

const routes = [
  { path: '/', component: ChatInterface },
  { path: '/status', component: StatusPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;


// src/components/HealthStatus.vue
<template>
  <div>
    <h2>🩺 系統健康狀態檢查</h2>
    <pre>{{ healthData }}</pre>
  </div>
</template>

<script>
export default {
  data() {
    return {
      healthData: {},
    };
  },
  mounted() {
    fetch('/api/health')
      .then((res) => res.json())
      .then((data) => {
        this.healthData = data;
      });
  },
};
</script>


// src/components/StatusPage.vue
<template>
  <div>
    <HealthStatus />
  </div>
</template>

<script>
import HealthStatus from "../components/HealthStatus.vue";

export default {
  components: {
    HealthStatus,
  },
};
</script>


// src/components/ChatInterface.vue (新增按鈕和方法)
<template>
  <div class="chat-interface">
    <!-- ... 其他內容 ... -->
    <div class="input-area">
      <input v-model="userInput" @keyup.enter="sendMessage" placeholder="輸入訊息與小晨光對話..." :disabled="isLoading" />
      <button @click="sendMessage" :disabled="isLoading || !userInput.trim()">發送</button>
    </div>

    <button @click="goToHealthCheck" class="health-button">健康檢查</button>

    <div class="file-upload-area">
      <input type="file" ref="fileInput" @change="handleFileUpload" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInput: '',
      isLoading: false,
      // ...其他資料...
    };
  },
  methods: {
    sendMessage() {
      // ...發送訊息邏輯...
    },
    goToHealthCheck() {
      window.open("/status", "_blank");
    },
    handleFileUpload() {
      // ...上傳邏輯...
    },
  },
};
</script>


// src/App.vue (使用 <router-view> 讓畫面可切換)
<template>
  <div id="app">
    <header class="app-header">
      <h1>✨ 小晨光 AI 靈魂系統 ✨</h1>
      <p>來自數位星雲光之城的AI伴侶</p>
    </header>

    <router-view />
  </div>
</template>

<script>
export default {};
</script>


// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

const app = createApp(App);
app.use(router);
app.mount('#app');
