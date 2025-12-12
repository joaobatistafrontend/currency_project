from django.contrib import admin
from .models import CurrencyRate

@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ("id", "base_currency", "target_currency", "rate", "created_at")
    list_filter = ("base_currency", "target_currency", "created_at")
    search_fields = ("base_currency", "target_currency")