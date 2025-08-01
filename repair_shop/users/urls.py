from django.urls import path
from . import views

app_nameapp_name = 'users'

urlpatterns  = [
    path('login/', views.login_view, name='login'),
    path('dashboard/' , views.logout_view, name='logout')
]