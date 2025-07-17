from django.contrib import admin
from .models import InventoryItem
# Register your models here.

@admin.register(InventoryItem)
class InventoryItemAdd (admin.ModelAdmin):
    list_display = [
        'name', 'part_number', 'quantity', 'note', 'location',
        'category'
    ]
    list_filter = ['location', 'category']
    search_fields = [
        'name', 'part_number', 'quantity', 'note', 'location',
        'category'
    ]
    ordering = ['name']