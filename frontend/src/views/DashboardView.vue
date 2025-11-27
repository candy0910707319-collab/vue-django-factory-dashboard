<template>
  <div class="dashboard">
    <el-card class="header-card">
      <h1>🏭 工廠資料儀表板</h1>
      <p>即時監控生產數據、設備狀態與警報事件</p>
    </el-card>

    <el-row :gutter="20" class="stats-row">
      <el-col :xs="24" :sm="12" :md="6">
        <el-card class="stat-card">
          <div class="stat-content">
            <el-icon class="stat-icon" :size="40" color="#409EFF">
              <Document />
            </el-icon>
            <div class="stat-text">
              <div class="stat-value">1,234</div>
              <div class="stat-label">總產量</div>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :xs="24" :sm="12" :md="6">
        <el-card class="stat-card">
          <div class="stat-content">
            <el-icon class="stat-icon" :size="40" color="#67C23A">
              <Check />
            </el-icon>
            <div class="stat-text">
              <div class="stat-value">98.5%</div>
              <div class="stat-label">平均良率</div>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :xs="24" :sm="12" :md="6">
        <el-card class="stat-card">
          <div class="stat-content">
            <el-icon class="stat-icon" :size="40" color="#E6A23C">
              <Setting />
            </el-icon>
            <div class="stat-text">
              <div class="stat-value">12</div>
              <div class="stat-label">運轉設備</div>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :xs="24" :sm="12" :md="6">
        <el-card class="stat-card">
          <div class="stat-content">
            <el-icon class="stat-icon" :size="40" color="#F56C6C">
              <Warning />
            </el-icon>
            <div class="stat-text">
              <div class="stat-value">3</div>
              <div class="stat-label">待處理警報</div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20" class="charts-row">
      <el-col :xs="24" :md="12">
        <el-card>
          <template #header>
            <h3>📈 生產趨勢</h3>
          </template>
          <div class="chart-placeholder">
            圖表元件開發中...
          </div>
        </el-card>
      </el-col>
      <el-col :xs="24" :md="12">
        <el-card>
          <template #header>
            <h3>🔧 設備狀態</h3>
          </template>
          <div class="chart-placeholder">
            圖表元件開發中...
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-row class="table-row">
      <el-col :span="24">
        <el-card>
          <template #header>
            <h3>⚠️ 最新警報</h3>
          </template>
          <el-table :data="[]" style="width: 100%">
            <el-table-column prop="level" label="等級" width="100" />
            <el-table-column prop="equipment" label="設備" width="150" />
            <el-table-column prop="message" label="訊息" />
            <el-table-column prop="createdAt" label="時間" width="180" />
          </el-table>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useFactoryStore } from '@/stores/factory'
import { Document, Check, Setting, Warning } from '@element-plus/icons-vue'

const factoryStore = useFactoryStore()

onMounted(() => {
  factoryStore.fetchDashboardData()
})
</script>

<style scoped lang="scss">
.dashboard {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

.header-card {
  margin-bottom: 20px;
  text-align: center;

  h1 {
    margin: 0 0 10px 0;
    color: #303133;
  }

  p {
    margin: 0;
    color: #909399;
  }
}

.stats-row {
  margin-bottom: 20px;
}

.stat-card {
  margin-bottom: 20px;
}

.stat-content {
  display: flex;
  align-items: center;
  gap: 20px;
}

.stat-icon {
  flex-shrink: 0;
}

.stat-text {
  flex: 1;
}

.stat-value {
  font-size: 28px;
  font-weight: bold;
  color: #303133;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 14px;
  color: #909399;
}

.charts-row {
  margin-bottom: 20px;
}

.chart-placeholder {
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f7fa;
  border-radius: 4px;
  color: #909399;
}

.table-row {
  margin-bottom: 20px;
}
</style>
