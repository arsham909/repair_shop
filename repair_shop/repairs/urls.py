from django.urls import path
from . import views

app_name = 'repairs'

urlpatterns = [
    path('', views.jobs, name='repairs'),
    path('addrepairs/', views.AddRepairs, name='addrepairs'),
    path('thanks/', views.thanks, name='thanks'),
    
    path('addcompany/', views.AddCompany_view, name='addcompany'),
    path('companies/list/',views.list_companies, name='companies_list'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('company/edit/<int:pk>', views.company_edit, name='company_edit'),
    path('company/delete/<int:pk>', views.compnay_delete, name='component_delete'),
    
]