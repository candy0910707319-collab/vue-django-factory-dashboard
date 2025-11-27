from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models
from .models import ProductionData, Equipment, Alert
from .serializers import ProductionDataSerializer, EquipmentSerializer, AlertSerializer


class ProductionDataViewSet(viewsets.ModelViewSet):
    """生產資料 API"""
    queryset = ProductionData.objects.all()
    serializer_class = ProductionDataSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    """設備資料 API"""
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class AlertViewSet(viewsets.ModelViewSet):
    """警報事件 API"""
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


@api_view(['GET'])
def dashboard_stats(request):
    """儀表板統計資料"""
    total_production = ProductionData.objects.count()
    active_equipment = Equipment.objects.filter(status='running').count()
    pending_alerts = Alert.objects.filter(resolved_at__isnull=True).count()
    
    # 計算平均良率
    avg_yield = ProductionData.objects.aggregate(
        models.Avg('yield_rate')
    )['yield_rate__avg'] or 0
    
    return Response({
        'totalProduction': total_production,
        'averageYieldRate': round(avg_yield, 2),
        'activeEquipment': active_equipment,
        'pendingAlerts': pending_alerts,
    })
