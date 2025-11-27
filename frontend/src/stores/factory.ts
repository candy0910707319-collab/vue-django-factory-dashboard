import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { ProductionData, Equipment, Alert } from '@/types/factory'

export const useFactoryStore = defineStore('factory', () => {
  const productionData = ref<ProductionData[]>([])
  const equipment = ref<Equipment[]>([])
  const alerts = ref<Alert[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  const fetchDashboardData = async () => {
    loading.value = true
    error.value = null
    try {
      // TODO: 實作 API 呼叫
      // const response = await factoryApi.getDashboardStats()
      // productionData.value = response.data.production
      // equipment.value = response.data.equipment
      // alerts.value = response.data.alerts
      
      // 暫時使用 mock 資料
      console.log('Fetching dashboard data...')
    } catch (err) {
      error.value = err instanceof Error ? err.message : '未知錯誤'
    } finally {
      loading.value = false
    }
  }

  return {
    productionData,
    equipment,
    alerts,
    loading,
    error,
    fetchDashboardData,
  }
})
