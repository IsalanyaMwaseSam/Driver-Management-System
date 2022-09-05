from django.contrib import admin
from django.urls import path
from . import views
from .views import StaffView, CarView


urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('staff/', StaffView.as_view(), name='staffview'),
    path('car_reg/', views.car_reg, name='car_reg'),
    path('profile/', views.profile, name='profile'),
    path('cars/', CarView.as_view(), name='cars'),
    path('payment/', views.payment, name='payment'),
    path('pay/', views.pay, name='pay'),
    path('ownerspay/', views.ownerspay, name='ownerspay'),
    path('driverspending/', views.driverspending, name='driverspending'),
    path('delete_user/<account_id>', views.delete_user, name='delete_user'),
    path('delete_car/<car_id>', views.delete_car, name='delete_car'),
    path('paypal-return/', views.PaypalReturnView.as_view(), name='paypal-return'),
    path('paypal-cancel/', views.PaypalCancelView.as_view(), name='paypal-cancel'),
    path('new-payments/', views.new_payment, name='new-payments'),
]