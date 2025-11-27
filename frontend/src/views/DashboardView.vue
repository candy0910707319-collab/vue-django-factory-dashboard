<template>
  <div class="api-test">
    <h1>API 連接測試</h1>
    
    <el-card>
      <h2>測試後端 API 連接</h2>
      
      <el-space direction="vertical" style="width: 100%">
        <el-button type="primary" @click="testConnection" :loading="loading">
          測試連接
        </el-button>

        <el-button @click="fetchProduction" :loading="loading">
          獲取生產資料
        </el-button>

        <el-button @click="fetchEquipment" :loading="loading">
          獲取設備資料
        </el-button>

        <el-button @click="fetchAlerts" :loading="loading">
          獲取警報資料
        </el-button>
      </el-space>

      <el-divider />

      <div v-if="error" class="error-box">
        <h3>錯誤訊息：</h3>
        <pre>{{ error }}</pre>
      </div>

      <div v-if="response" class="response-box">
        <h3>API 回應：</h3>
        <pre>{{ JSON.stringify(response, null, 2) }}</pre>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { factoryApi } from '@/services/factoryApi'

const loading = ref(false)
const error = ref<string | null>(null)
const response = ref<any>(null)

const testConnection = async () => {
  loading.value = true
  error.value = null
  response.value = null
  
  try {
    // 測試基本連接
    const res = await factoryApi.getDashboardStats()
    response.value = res.data
  } catch (err: any) {
    error.value = err.message || '連接失敗'
    console.error('API Error:', err)
  } finally {
    loading.value = false
  }
}

const fetchProduction = async () => {
  loading.value = true
  error.value = null
  response.value = null
  
  try {
    const res = await factoryApi.getProduction()
    response.value = res.data
  } catch (err: any) {
    error.value = err.message || '獲取生產資料失敗'
  } finally {
    loading.value = false
  }
}

const fetchEquipment = async () => {
  loading.value = true
  error.value = null
  response.value = null
  
  try {
    const res = await factoryApi.getEquipment()
    response.value = res.data
  } catch (err: any) {
    error.value = err.message || '獲取設備資料失敗'
  } finally {
    loading.value = false
  }
}

const fetchAlerts = async () => {
  loading.value = true
  error.value = null
  response.value = null
  
  try {
    const res = await factoryApi.getAlerts()
    response.value = res.data
  } catch (err: any) {
    error.value = err.message || '獲取警報資料失敗'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.api-test {
  padding: 40px;
  max-width: 1000px;
  margin: 0 auto;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
}

h2 {
  margin-bottom: 20px;
}

.error-box {
  padding: 20px;
  background-color: #fef0f0;
  border: 1px solid #f56c6c;
  border-radius: 4px;
  margin-top: 20px;
}

.error-box h3 {
  color: #f56c6c;
  margin-bottom: 10px;
}

.response-box {
  padding: 20px;
  background-color: #f0f9ff;
  border: 1px solid #409eff;
  border-radius: 4px;
  margin-top: 20px;
}

.response-box h3 {
  color: #409eff;
  margin-bottom: 10px;
}

pre {
  margin: 0;
  white-space: pre-wrap;
  word-wrap: break-word;
  font-family: 'Courier New', monospace;
  font-size: 14px;
}
</style>
