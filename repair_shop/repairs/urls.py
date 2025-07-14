from django.urls import path
from . import views

app_name = 'repairs'

urlpatterns = [
    path('', views.jobs, name='jobs')
    
]