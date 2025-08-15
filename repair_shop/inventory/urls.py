from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns  = [
    path('', views.inventory, name='inventory'),
    path('AddComponents/', views.add_components, name='AddComponents'),
    path('thanks/', views.thanks, name='thanks'),
    path('search/components/', views.searchcomponent, name='search_component'),
]