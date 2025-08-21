from django.contrib import admin
from .models import Repair , Company
# Register your models here.

# class RepairInLine(admin.TabularInline):
#     model = RepairJobs
    

# @admin.register(RepairJobs)
# class RepairAdmin(admin.ModelAdmin):
#     list_display = ['job_number', 'device_name',
#                     'device_part_number', 'assigned_to',
#                     'parts_needs']
#     list_filter = ['status', 'date', 'assigned_to', 'brand']
#     search_fields = ['job_number', 'device_name',
#                     'device_part_number', 'assigned_to',
#                     'parts_needs', 'notes',
#                     'brand']
#     #date_hierarchy = ['date']
#     ordering = ['status', 'date']
#     #raw_id_fields = ['assigned_to']
    
# @admin.register(Company)
# class CompanyAdmin( admin.ModelAdmin):
#     list_display = ['name' , 'address' , 'phonenumber']
#     inlines = [RepairInLine]