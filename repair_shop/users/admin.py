from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
# Register your models here.

#should use admin.ModelAdmin for model that you used abstract model in it 
@admin.register(Users)
class Users_account(UserAdmin):
    list_display = ['username']