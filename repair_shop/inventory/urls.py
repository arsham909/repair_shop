from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns  = [
    path('', views.inventory, name='inventory'),
    path('AddComponents/', views.add_components, name='AddComponents'),
    path('component/<int:pk>', views.component_detail, name='component_detail' ),
    path('component/<int:pk>/edit', views.component_edit, name='component_edit' ),
    path('component/<int:pk>/delete', views.component_delete, name='component_delete' ),
    path('search/components/', views.searchcomponent, name='search_component'),
    path('thanks/', views.thanks, name='thanks'),
]