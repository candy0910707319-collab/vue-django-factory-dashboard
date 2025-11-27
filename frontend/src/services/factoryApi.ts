import apiClient from './api'
import type { ProductionData, Equipment, Alert, DashboardStats } from '@/types/factory'

/**
 * 工廠資料 API 服務
 */
export const factoryApi = {
  /**
   * 獲取生產資料列表
   */
  getProduction: () => {
    return apiClient.get<ProductionData[]>('/factory/production/')
  },

  /**
   * 獲取設備狀態列表
   */
  getEquipment: () => {
    return apiClient.get<Equipment[]>('/factory/equipment/')
  },

  /**
   * 獲取警報事件列表
   */
  getAlerts: () => {
    return apiClient.get<Alert[]>('/factory/alerts/')
  },

  /**
   * 獲取儀表板統計資料
   */
  getDashboardStats: () => {
    return apiClient.get<DashboardStats>('/factory/dashboard/stats/')
  },
}
