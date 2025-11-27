/**
 * 生產資料類型定義
 */
export interface ProductionData {
  id: number
  timestamp: string
  lineId: string
  output: number
  yieldRate: number
}

/**
 * 設備資料類型定義
 */
export interface Equipment {
  id: number
  equipmentId: string
  name: string
  status: 'running' | 'stopped' | 'maintenance' | 'error'
  temperature?: number
  vibration?: number
  powerConsumption?: number
}

/**
 * 警報事件類型定義
 */
export interface Alert {
  id: number
  equipmentId: number
  level: 'info' | 'warning' | 'error' | 'critical'
  message: string
  createdAt: string
  resolvedAt?: string
}

/**
 * 儀表板統計資料
 */
export interface DashboardStats {
  totalProduction: number
  averageYieldRate: number
  activeEquipment: number
  pendingAlerts: number
}
