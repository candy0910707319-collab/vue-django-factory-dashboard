from django.contrib import admin
from .models import ProductionData, Equipment, Alert


@admin.register(ProductionData)
class ProductionDataAdmin(admin.ModelAdmin):
    list_display = ('line_id', 'output', 'yield_rate', 'timestamp')
    list_filter = ('line_id', 'timestamp')
    search_fields = ('line_id',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipment_id', 'name', 'status', 'temperature')
    list_filter = ('status',)
    search_fields = ('equipment_id', 'name')


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'level', 'message', 'created_at', 'resolved_at')
    list_filter = ('level', 'created_at')
    search_fields = ('message',)
