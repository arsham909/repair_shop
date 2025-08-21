from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
# Register your models here.

#should use admin.ModelAdmin for model that you used abstract model in it 
@admin.register(Users)
class Users_account(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('additional info' , {'fields':('role',)}),
        )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('additional info' , {'fields':('role',)}),
    )
    list_display = ['username', 'role']