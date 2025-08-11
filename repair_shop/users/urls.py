from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_nameapp_name = 'users'

urlpatterns  = [
    # path('login/', views.login_view, name='login'),
    # path('dashboard/' , views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/' ,auth_views.PasswordChangeView.as_view(), name='changepassword'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.dashboard , name='dashboard'),
]