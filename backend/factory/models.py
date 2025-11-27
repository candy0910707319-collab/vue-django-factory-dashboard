from django.db import models


class ProductionData(models.Model):
    """生產資料模型"""
    timestamp = models.DateTimeField(auto_now_add=True)
    line_id = models.CharField(max_length=50, verbose_name='生產線ID')
    output = models.IntegerField(verbose_name='產量')
    yield_rate = models.FloatField(verbose_name='良率')

    class Meta:
        verbose_name = '生產資料'
        verbose_name_plural = '生產資料'
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.line_id} - {self.timestamp}"


class Equipment(models.Model):
    """設備資料模型"""
    STATUS_CHOICES = [
        ('running', '運轉中'),
        ('stopped', '停止'),
        ('maintenance', '維護中'),
        ('error', '故障'),
    ]

    equipment_id = models.CharField(max_length=50, unique=True, verbose_name='設備ID')
    name = models.CharField(max_length=100, verbose_name='設備名稱')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='狀態')
    temperature = models.FloatField(null=True, blank=True, verbose_name='溫度')
    vibration = models.FloatField(null=True, blank=True, verbose_name='震動')
    power_consumption = models.FloatField(null=True, blank=True, verbose_name='能耗')

    class Meta:
        verbose_name = '設備'
        verbose_name_plural = '設備'

    def __str__(self):
        return f"{self.name} ({self.equipment_id})"


class Alert(models.Model):
    """警報事件模型"""
    LEVEL_CHOICES = [
        ('info', '資訊'),
        ('warning', '警告'),
        ('error', '錯誤'),
        ('critical', '嚴重'),
    ]

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='設備')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name='等級')
    message = models.TextField(verbose_name='訊息')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='建立時間')
    resolved_at = models.DateTimeField(null=True, blank=True, verbose_name='解決時間')

    class Meta:
        verbose_name = '警報'
        verbose_name_plural = '警報'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.level} - {self.equipment.name}"
