from django.urls import path
from . import views

app_name = 'repairs'

urlpatterns = [
    path('', views.jobs, name='repairs'),
    path('addrepairs/', views.AddRepairs, name='addrepairs'),
    path('thanks/', views.thanks, name='thanks'),
    path('addcompany/', views.AddCompany_view, name='addcompany'),
    path('companies/list/',views.list_companies, name='companieslist')
    
]