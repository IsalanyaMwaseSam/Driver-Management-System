from django.contrib import admin
from django.urls import path
from . import views
from .views import StaffView, CarView


urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('staff/', views.staff, name='staff'),
    path('staffview/', StaffView.as_view(), name='staffview'),
    path('cars/', views.cars, name='cars'),
    path('car_reg/', views.car_reg, name='car_reg'),
    path('profile/', views.profile, name='profile'),
    path('carview/', CarView.as_view(), name='carview'),
    path('payment/', views.payment, name='payment'),
    path('pay/', views.pay, name='pay'),
    path('ownerspay/', views.ownerspay, name='ownerspay'),
    path('driverspending/', views.driverspending, name='driverspending'),
    path('delete_user/<account_id>', views.delete_user, name='delete_user'),
]