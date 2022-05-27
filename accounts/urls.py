from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from . import views as user_views
from . import views

urlpatterns = [
    path('accounts/register', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    
]