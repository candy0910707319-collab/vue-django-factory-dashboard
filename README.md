# 🏭 Vue + Django 工廠資料儀表板

使用 Vue 3 + Django REST Framework 建立的工廠即時監控儀表板系統

## 技術堆疊

### 前端
- Vue 3 + TypeScript + Vite
- Pinia (狀態管理)
- ECharts (圖表)
- Element Plus (UI 元件)

### 後端
- Django 4.x
- Django REST Framework
- PostgreSQL
- JWT 認證

## 專案結構

```
Vue Web/
├── frontend/          # Vue 前端
├── backend/           # Django 後端
├── docs/              # 文件
└── mock/              # Mock 資料
```

## 快速開始

### 前端開發
```bash
cd frontend
npm install
npm run dev
```

### 後端開發
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

## 功能特色

- 📊 即時生產數據圖表
- 🏭 設備狀態監控
- ⚠️ 警報事件通知
- 📈 KPI 關鍵指標

## 開發進度

詳見 [專案計劃](docs/project-plan.md)

## 授權

MIT License