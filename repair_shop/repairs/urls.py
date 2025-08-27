from django.urls import path
from . import views
from .views import CheckIn , assign_requested

app_name = 'repairs'

urlpatterns = [
    path('', views.jobs, name='repairs'),
    # path('addrepairs/', views.AddRepairs, name='addrepairs'),
    path('thanks/', views.thanks, name='thanks'),
    #field for state machine
    path('checkin/', CheckIn.as_view(), name='check_in'),
    path('assign-request', assign_requested.as_view(), name='assign-request'),
    
    #path for repairs jobs
    path('list/', views.Repairs_list.as_view(), name='repairs_list'),
    
    path('clients/', views.Clients.as_view(), name='clients_list'),
    path('client/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/edit/', views.ClientEditView.as_view(), name='client_edit'),
    # path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_create'),
    
    path('addcompany/', views.AddCompany_view, name='addcompany'),
    path('companies/list/',views.list_companies, name='companies_list'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('company/edit/<int:pk>', views.company_edit, name='company_edit'),
    path('company/delete/<int:pk>', views.compnay_delete, name='company_delete'),
    path('search/companies', views.search_company, name='search_companies' )
]