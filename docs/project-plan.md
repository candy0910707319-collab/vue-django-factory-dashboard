# Vue + Django 工廠資料儀表板專案計劃

## 專案概述
建立一個全端網站應用，使用 Vue 3 作為前端框架，Django 作為後端 API 伺服器，透過 RESTful API 獲取工廠營運資料，並在儀表板介面以圖形化方式呈現關鍵指標。

## 技術堆疊

### 前端 (Frontend)
- **框架**: Vue 3 (Composition API)
- **建置工具**: Vite
- **語言**: TypeScript
- **狀態管理**: Pinia
- **路由**: Vue Router
- **圖表庫**: ECharts / Chart.js
- **HTTP 客戶端**: Axios
- **UI 元件**: Element Plus / Ant Design Vue
- **測試**: Vitest + Vue Test Utils

### 後端 (Backend)
- **框架**: Django 4.x
- **REST API**: Django REST Framework (DRF)
- **資料庫**: PostgreSQL / MySQL / SQLite (開發用)
- **認證**: JWT (djangorestframework-simplejwt)
- **CORS**: django-cors-headers
- **環境管理**: python-dotenv
- **API 文件**: drf-spectacular (OpenAPI/Swagger)
- **測試**: pytest + pytest-django

## 專案結構

```
Vue Web/
├── frontend/                    # Vue 前端專案
│   ├── src/
│   │   ├── assets/             # 靜態資源
│   │   ├── components/         # 可重用元件
│   │   │   ├── charts/        # 圖表元件
│   │   │   ├── cards/         # 卡片元件
│   │   │   └── common/        # 通用元件
│   │   ├── views/             # 頁面視圖
│   │   │   └── DashboardView.vue
│   │   ├── router/            # 路由配置
│   │   ├── stores/            # Pinia 狀態管理
│   │   ├── services/          # API 服務層
│   │   │   └── factoryApi.ts
│   │   ├── types/             # TypeScript 型別定義
│   │   └── utils/             # 工具函數
│   ├── public/
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
│
├── backend/                     # Django 後端專案
│   ├── config/                 # Django 設定
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── factory/                # 工廠資料 App
│   │   ├── models.py          # 資料模型
│   │   ├── serializers.py     # DRF 序列化器
│   │   ├── views.py           # API 視圖
│   │   ├── urls.py            # API 路由
│   │   └── tests.py           # 測試
│   ├── manage.py
│   ├── requirements.txt
│   └── .env
│
├── docs/                        # 文件資料夾
│   ├── api-contract.md         # API 規格文件
│   └── architecture.md         # 架構圖
│
└── mock/                        # Mock 資料
    └── factory/
        ├── production.json
        ├── equipment.json
        └── alerts.json
```

## 開發階段規劃

### Phase 1: 專案初始化 (第 1 天)

#### 1.1 建立專案結構
- [ ] 建立 `frontend/` 和 `backend/` 資料夾
- [ ] 初始化 Git 版本控制
- [ ] 建立 `.gitignore` 檔案

#### 1.2 前端環境設定
```bash
cd frontend
npm create vite@latest . -- --template vue-ts
npm install
npm install vue-router pinia axios echarts element-plus
npm install -D @types/node sass vitest @vue/test-utils
```

#### 1.3 後端環境設定
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install django djangorestframework django-cors-headers
pip install djangorestframework-simplejwt python-dotenv
pip install drf-spectacular pytest pytest-django
django-admin startproject config .
python manage.py startapp factory
```

### Phase 2: API 規格設計 (第 1-2 天)

#### 2.1 定義資料模型
**工廠資料類型**:
- **生產資料**: 產量、良率、稼動率
- **設備狀態**: 運轉狀態、溫度、震動、能耗
- **品質指標**: 不良率、檢驗數據
- **警報事件**: 異常通知、維護提醒

#### 2.2 API 端點設計
```
GET  /api/factory/production/      # 生產數據列表
GET  /api/factory/production/{id}/  # 單筆生產數據
GET  /api/factory/equipment/        # 設備狀態列表
GET  /api/factory/alerts/           # 警報事件
GET  /api/factory/dashboard/stats/  # 儀表板統計摘要
POST /api/auth/token/               # 登入取得 JWT
POST /api/auth/token/refresh/       # 刷新 Token
```

#### 2.3 建立 Mock 資料
在 `mock/factory/` 建立 JSON 範例檔案供前端開發使用

### Phase 3: 後端開發 (第 2-4 天)

#### 3.1 Django 設定
```python
# settings.py 重點設定
INSTALLED_APPS = [
    'rest_framework',
    'corsheaders',
    'factory',
    'drf_spectacular',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Vite 開發伺服器
]
```

#### 3.2 建立資料模型
```python
# factory/models.py
class ProductionData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    line_id = models.CharField(max_length=50)
    output = models.IntegerField()
    yield_rate = models.FloatField()
    
class Equipment(models.Model):
    equipment_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    temperature = models.FloatField(null=True)
    
class Alert(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    level = models.CharField(max_length=20)  # warning, error, critical
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

#### 3.3 實作 API ViewSets
```python
# factory/views.py
from rest_framework import viewsets
from .models import ProductionData, Equipment, Alert
from .serializers import ProductionDataSerializer

class ProductionDataViewSet(viewsets.ModelViewSet):
    queryset = ProductionData.objects.all()
    serializer_class = ProductionDataSerializer
```

#### 3.4 測試與 API 文件
- 撰寫單元測試驗證 API 功能
- 設定 Swagger UI: `/api/schema/swagger-ui/`

### Phase 4: 前端開發 (第 4-7 天)

#### 4.1 建立 API 服務層
```typescript
// src/services/factoryApi.ts
import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

// 攔截器：自動加入 JWT Token
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export const factoryApi = {
  getProduction: () => apiClient.get('/factory/production/'),
  getEquipment: () => apiClient.get('/factory/equipment/'),
  getAlerts: () => apiClient.get('/factory/alerts/'),
  getDashboardStats: () => apiClient.get('/factory/dashboard/stats/'),
}
```

#### 4.2 Pinia Store 狀態管理
```typescript
// src/stores/factory.ts
import { defineStore } from 'pinia'
import { factoryApi } from '@/services/factoryApi'

export const useFactoryStore = defineStore('factory', {
  state: () => ({
    productionData: [],
    equipment: [],
    alerts: [],
    loading: false,
    error: null,
  }),
  
  actions: {
    async fetchDashboardData() {
      this.loading = true
      try {
        const [prod, equip, alerts] = await Promise.all([
          factoryApi.getProduction(),
          factoryApi.getEquipment(),
          factoryApi.getAlerts(),
        ])
        this.productionData = prod.data
        this.equipment = equip.data
        this.alerts = alerts.data
      } catch (err) {
        this.error = err
      } finally {
        this.loading = false
      }
    },
  },
})
```

#### 4.3 儀表板視圖元件
```vue
<!-- src/views/DashboardView.vue -->
<template>
  <div class="dashboard">
    <el-row :gutter="20">
      <el-col :span="6" v-for="stat in stats" :key="stat.title">
        <StatCard :title="stat.title" :value="stat.value" :icon="stat.icon" />
      </el-col>
    </el-row>
    
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :span="12">
        <ProductionChart :data="productionData" />
      </el-col>
      <el-col :span="12">
        <EquipmentStatusChart :data="equipment" />
      </el-col>
    </el-row>
    
    <el-row style="margin-top: 20px">
      <el-col :span="24">
        <AlertsTable :alerts="alerts" />
      </el-col>
    </el-row>
  </div>
</template>
```

#### 4.4 圖表元件開發
使用 ECharts 建立：
- **ProductionChart**: 生產趨勢折線圖
- **EquipmentStatusChart**: 設備狀態圓餅圖
- **YieldRateChart**: 良率長條圖
- **AlertsTable**: 警報事件表格

#### 4.5 響應式設計
- 使用 Grid 系統適配不同螢幕尺寸
- Mobile-first 設計原則
- 斷點設定：手機 (<768px)、平板 (768-1024px)、桌面 (>1024px)

### Phase 5: 整合與測試 (第 7-8 天)

#### 5.1 前後端整合
- 啟動 Django 開發伺服器: `python manage.py runserver`
- 啟動 Vue 開發伺服器: `npm run dev`
- 測試 API 連線與資料流

#### 5.2 錯誤處理機制
- API 請求失敗重試邏輯
- 全域錯誤提示元件
- 載入狀態與骨架屏

#### 5.3 效能優化
- 前端：懶加載、元件快取、防抖節流
- 後端：資料庫索引、查詢優化、快取策略

#### 5.4 測試
- 前端：元件單元測試、E2E 測試
- 後端：API 整合測試、資料驗證測試

### Phase 6: 部署準備 (第 9-10 天)

#### 6.1 前端建置
```bash
cd frontend
npm run build
# 產生 dist/ 資料夾供部署
```

#### 6.2 後端設定
- 環境變數管理 (.env)
- 靜態檔案收集: `python manage.py collectstatic`
- 資料庫遷移: `python manage.py migrate`

#### 6.3 部署選項
- **前端**: Vercel、Netlify、Nginx
- **後端**: Docker + Gunicorn、Railway、DigitalOcean
- **資料庫**: PostgreSQL (Supabase、AWS RDS)

## 關鍵功能特性

### 儀表板功能
1. **即時資料更新**: WebSocket 或定時輪詢 (每 30 秒)
2. **資料篩選**: 時間範圍、生產線、設備選擇
3. **資料匯出**: CSV / Excel 格式
4. **警報通知**: 瀏覽器通知 API
5. **使用者權限**: 讀取者、操作員、管理員

### 資料視覺化元件
- 生產趨勢折線圖 (近 24 小時)
- 設備即時狀態儀表板
- 良率分析長條圖
- 警報事件時間軸
- KPI 數字卡片 (產量、良率、稼動率)

## 開發環境需求

### 必要工具
- Node.js 18+ 
- Python 3.10+
- PostgreSQL 14+ (或 SQLite 開發用)
- Git
- VS Code (推薦)

### VS Code 推薦擴充
- Vue - Official
- Python
- Pylance
- REST Client
- ESLint
- Prettier

## 安全性考量

1. **認證授權**: JWT Token、CORS 設定
2. **輸入驗證**: DRF Serializer 驗證、前端表單驗證
3. **SQL Injection 防護**: Django ORM 參數化查詢
4. **XSS 防護**: Vue 自動轉義、CSP 標頭
5. **環境變數**: 敏感資訊 (API Key、資料庫密碼) 不進版控

## 後續擴充功能

- [ ] 多語系支援 (i18n)
- [ ] 深色模式切換
- [ ] 歷史資料查詢與分析
- [ ] 預測性維護演算法
- [ ] 行動裝置 App (React Native)
- [ ] 郵件/簡訊警報通知
- [ ] 儀表板自訂配置儲存

## 參考資源

- [Vue 3 官方文件](https://vuejs.org/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [ECharts 範例](https://echarts.apache.org/examples/)
- [Element Plus 元件庫](https://element-plus.org/)

---

**預計開發時程**: 10 個工作天  
**團隊規模**: 1-2 名全端工程師  
**交付項目**: 可運行的原型系統 + API 文件 + 部署指南
