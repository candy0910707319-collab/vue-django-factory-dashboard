<template>
  <div class="factory-system">
    <!-- 側邊欄 -->
    <aside class="sidebar">
      <div class="logo">
        <h2>🏭 工廠系統</h2>
      </div>
      <el-menu
        :default-active="activeMenu"
        class="sidebar-menu"
        background-color="#1e88e5"
        text-color="#ffffff"
        active-text-color="#ffffff"
      >
        <el-menu-item index="1" @click="activeMenu = '1'">
          <el-icon><HomeFilled /></el-icon>
          <span>首頁</span>
        </el-menu-item>
        <el-menu-item index="2" @click="activeMenu = '2'">
          <el-icon><User /></el-icon>
          <span>員工管理</span>
        </el-menu-item>
        <el-menu-item index="3" @click="activeMenu = '3'">
          <el-icon><TrendCharts /></el-icon>
          <span>生產管理</span>
        </el-menu-item>
        <el-menu-item index="4" @click="activeMenu = '4'">
          <el-icon><Document /></el-icon>
          <span>工單管理</span>
        </el-menu-item>
      </el-menu>
    </aside>

    <!-- 主內容區 -->
    <main class="main-content">
      <!-- 頂部欄 -->
      <header class="top-bar">
        <div class="breadcrumb">
          <span>首頁</span>
        </div>
        <div class="user-info">
          <span>葉桓臻</span>
        </div>
      </header>

      <!-- 內容 -->
      <div class="content">
        <h1 class="page-title">系統儀表板</h1>
        <p class="page-subtitle">歡迎使用工廠管理系統</p>

        <!-- 統計卡片 -->
        <div class="stats-grid">
          <div class="stat-card cyan">
            <div class="stat-content">
              <div class="stat-info">
                <h3>工單數量</h3>
                <div class="stat-value">{{ stats.workOrders }}</div>
                <div class="stat-unit">張</div>
              </div>
              <div class="stat-icon">
                <el-icon :size="80"><Document /></el-icon>
              </div>
            </div>
          </div>

          <div class="stat-card green">
            <div class="stat-content">
              <div class="stat-info">
                <h3>員工</h3>
                <div class="stat-value">{{ stats.employees }}</div>
                <div class="stat-unit">人</div>
              </div>
              <div class="stat-icon">
                <el-icon :size="80"><User /></el-icon>
              </div>
            </div>
          </div>

          <div class="stat-card yellow">
            <div class="stat-content">
              <div class="stat-info">
                <h3>產量</h3>
                <div class="stat-value">{{ stats.production }}</div>
                <div class="stat-unit">件</div>
              </div>
              <div class="stat-icon">
                <el-icon :size="80"><TrendCharts /></el-icon>
              </div>
            </div>
          </div>

          <div class="stat-card red">
            <div class="stat-content">
              <div class="stat-info">
                <h3>設備</h3>
                <div class="stat-value">{{ stats.equipment }}</div>
                <div class="stat-unit">台</div>
              </div>
              <div class="stat-icon">
                <el-icon :size="80"><Setting /></el-icon>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { HomeFilled, User, TrendCharts, Document, Setting } from '@element-plus/icons-vue'
import { factoryApi } from '@/services/factoryApi'

const activeMenu = ref('1')

const stats = ref({
  workOrders: 0,
  employees: 5,
  production: 0,
  equipment: 0
})

onMounted(async () => {
  try {
    const res = await factoryApi.getDashboardStats()
    stats.value = {
      workOrders: res.data.totalProduction || 0,
      employees: 5,
      production: res.data.totalProduction || 0,
      equipment: res.data.activeEquipment || 0
    }
  } catch (err) {
    console.error('載入統計資料失敗:', err)
  }
})
</script>

<style scoped>
.factory-system {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

/* 側邊欄 */
.sidebar {
  width: 200px;
  background: linear-gradient(180deg, #1e88e5 0%, #1565c0 100%);
  color: white;
  display: flex;
  flex-direction: column;
}

.logo {
  padding: 20px;
  text-align: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.logo h2 {
  margin: 0;
  font-size: 18px;
  color: white;
}

.sidebar-menu {
  flex: 1;
  border: none;
}

.sidebar-menu .el-menu-item {
  height: 56px;
  line-height: 56px;
}

.sidebar-menu .el-menu-item:hover {
  background-color: rgba(255, 255, 255, 0.1) !important;
}

.sidebar-menu .el-menu-item.is-active {
  background-color: rgba(255, 255, 255, 0.2) !important;
}

/* 主內容區 */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #f5f5f5;
  overflow: auto;
}

/* 頂部欄 */
.top-bar {
  height: 60px;
  background: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 30px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.breadcrumb {
  font-size: 14px;
  color: #666;
}

.user-info {
  font-size: 14px;
  color: #333;
}

/* 內容區 */
.content {
  padding: 30px;
  flex: 1;
}

.page-title {
  font-size: 28px;
  color: #333;
  margin: 0 0 10px 0;
}

.page-subtitle {
  font-size: 14px;
  color: #666;
  margin: 0 0 30px 0;
}

/* 統計卡片網格 */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

.stat-card {
  border-radius: 8px;
  padding: 30px;
  color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.stat-card.cyan {
  background: linear-gradient(135deg, #00bcd4 0%, #00acc1 100%);
}

.stat-card.green {
  background: linear-gradient(135deg, #4caf50 0%, #43a047 100%);
}

.stat-card.yellow {
  background: linear-gradient(135deg, #ffc107 0%, #ffa000 100%);
}

.stat-card.red {
  background: linear-gradient(135deg, #f44336 0%, #e53935 100%);
}

.stat-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.stat-info h3 {
  margin: 0 0 15px 0;
  font-size: 16px;
  font-weight: normal;
  opacity: 0.9;
}

.stat-value {
  font-size: 48px;
  font-weight: bold;
  line-height: 1;
  margin-bottom: 5px;
}

.stat-unit {
  font-size: 14px;
  opacity: 0.8;
}

.stat-icon {
  opacity: 0.3;
}
</style>
