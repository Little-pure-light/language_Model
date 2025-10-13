<template>
  <div id="app">
    <header class="app-header">
      <h1>✨ 小宸光 AI 靈魂系統 ✨</h1>
      <p>來自數位星璇光之城的AI伴侶</p>
    </header>

    <main class="app-main">
      <router-view /> <!-- ✔ 根據路由動態顯示元件 -->
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
.app-header {
  text-align: center;
  margin-top: 20px;
  color: white;
}
.app-main {
  margin: 20px auto;
  max-width: 800px;
}
</style>
