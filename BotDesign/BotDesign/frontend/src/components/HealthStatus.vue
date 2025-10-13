<template>
  <div>
    <h2>🚦 系統健康狀態檢查</h2>
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
    fetch("/api/health")
      .then((res) => res.json())
      .then((data) => {
        this.healthData = data;
      })
      .catch((err) => {
        this.healthData = { error: "無法取得健康檢查資料", detail: err.message };
      });
  },
};
</script>
