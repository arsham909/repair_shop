from django.urls import path
from . import views
from .views import CheckIn , Assigning, Evaluating, Qouting, Approved, Repairing, Shipper, Shipped

app_name = 'repairs'

urlpatterns = [
    path('', views.jobs, name='repairs'),
    # path('addrepairs/', views.AddRepairs, name='addrepairs'),
    path('thanks/', views.thanks, name='thanks'),
    #field for state machine
    path('checkin/', CheckIn.as_view(), name='check_in'),
    path('assigning/<int:pk>/', Assigning.as_view(), name='assigning'),
    path('evaluating/<int:pk>/', Evaluating.as_view(), name='evaluating'),
    path('qouting/<int:pk>/', Qouting.as_view(), name='qouting'),
    path('qouted/<int:pk>/', Qouting.as_view(), name='qouted'),
    path('approved/<int:pk>/', Approved.as_view(), name='approved'),
    path('repairing/<int:pk>/', Assigning.as_view(), name='repairing'),
    path('repaired/<int:pk>/', Repairing.as_view(), name='repaired'),
    path('shipping/<int:pk>/', Shipper.as_view(), name='shipper'),
    path('shipping/<int:pk>/', Shipper.as_view(), name='approveds'),
    path('done/<int:pk>/', Shipped.as_view(), name='done'),
    
    #path for repairs jobs
    path('list/', views.Repairs_list.as_view(), name='repairs_list'),
    path('detail/<int:pk>/', views.Repair_detail.as_view(), name='repair_detail'),
    path('search/repairs/', views.RepairSearch.as_view(), name='search_repairs'),
    
    path('clients/', views.Clients.as_view(), name='clients_list'),
    path('client/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/edit/', views.ClientEditView.as_view(), name='client_edit'),
    # path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_create'),
    path('search/clients/', views.ClientsSearch.as_view(), name='search_clients' ),
    
    path('addcompany/', views.AddCompany_view, name='addcompany'),
    path('companies/list/',views.list_companies, name='companies_list'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('company/edit/<int:pk>', views.company_edit, name='company_edit'),
    path('company/delete/<int:pk>', views.compnay_delete, name='company_delete'),
    path('search/companies', views.search_company, name='search_companies' )
]