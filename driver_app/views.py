from ast import Delete
from django.shortcuts import render, redirect
from accounts.models import *
from driver_app.models import Info, Payment
from .forms import *
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm




# Create your views here.
def home(request):
    queryset = Info.objects.all()
    staff = Account.objects.all()
    payment = Payment.objects.all()
    cars = Cars.objects.all()
    staff_count = staff.count()
    car_count = cars.count()
    payment_count = payment.count()
    context = {'queryset':queryset,
                'staff': staff,
                'staff_count': staff_count,
                'car_count': car_count,
                'payment_count': payment_count
    }
    return render(request, 'driver_app/owner.html', context)

def landing(request):
    return render(request, 'driver_app/home.html', {})


def car_reg(request):
    form = CarRegForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Car successfully registered!')
            return redirect('home')
        else:
            print('Form is not valid')
            print(form.errors)
    context = {'form':form}
    return render(request, 'driver_app/car_reg.html', context)

def profile(request):
    form = UpdateUserForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated!')
            return redirect('home')
    context = {'form':form}
    return render(request, 'driver_app/profile.html', context)

class StaffView(ListView):
    model = Account
    template_name = 'driver_app/staff.html'
    paginate_by = 6
    



class CarView(ListView):
    model = Cars
    paginate_by = 6
    template_name = 'driver_app/cars.html'


class paymentView(ListView):
    model = Payment
    paginate_by = 6
    template_name = 'driver_app/payment.html' 

    def get_queryset(self):
        return Payment.objects.filter(driver=self.request.user)


def pay(request):
    return render(request, 'driver_app/pay.html', {}) 

class pendingView(ListView):
    model = Payment
    paginate_by = 6
    template_name = 'driver_app/driverspending.html' 

    def get_queryset(self):
        return Payment.objects.filter(driver=self.request.user) 

def delete_user(request, account_id):
    account = Account.objects.get(pk=account_id)
    account.delete()
    messages.success(request, 'User successfully deleted!')
    return redirect('staffview')

def delete_car(request, car_id):
    car = Cars.objects.get(pk=car_id)
    car.delete()
    messages.success(request, 'Car successfully deleted!')
    return redirect('carview')

class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'

class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'

class PaypalFormView(FormView):
    template_name = 'driver_app/paypal_form.html'
    form_class = PayPalPaymentsForm

    def get_initial(self):
        return {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": '20.00',
            "currency_code": "USD",
            "item_name": 'Example item',
            "invoice": 1234,
            "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": self.request.build_absolute_uri(reverse('paypal-return')),
            "cancel_return": self.request.build_absolute_uri(reverse('paypal-cancel')),
            "lc": 'EN',
            "no_shipping": '1',
        }

def new_payment(request):
    form = PaymentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment successfully registered!')
            return redirect('home')
    context = {'form':form}
    return render(request, 'driver_app/admin_new_payments.html', context)

class PaymentView(ListView):
    model = Payment
    paginate_by = 6
    template_name = 'driver_app/admin_complete_payments.html'


class PendingPaymentView(ListView):
    model = Payment
    paginate_by = 6
    template_name = 'driver_app/admin_pending_payments.html'

def createnotifications(request):
    return render(request, 'driver_app/create_notifications.html', {})

def notification(request):
    info = Info.objects.all()
    notifications = Info.objects.all()
    notification_count = notifications.count()
    context = {
        'info': info,
        'notifications': notifications,
        'notification_count': notification_count
    }
    return render(request, 'driver_app/notifications.html', context)

def new_notification(request):
    form = NotificationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'New notification posted!')
            return redirect('home')
    context = {'form':form}
    return render(request, 'driver_app/admin_notifications.html', context)

def statistics(request):
    return render(request, 'driver_app/stats.html', {}) 