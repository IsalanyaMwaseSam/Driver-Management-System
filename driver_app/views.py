from django.shortcuts import render, redirect
from accounts.models import *
from driver_app.models import Info
from .forms import *
from django.contrib import messages
from django.views.generic import ListView



# Create your views here.
def home(request):
    queryset = Info.objects.all()
    context = {'queryset':queryset}
    return render(request, 'driver_app/owner.html', context)

def landing(request):
    return render(request, 'driver_app/home.html', {})

def staff(request):
    return render(request, 'driver_app/staff.html', {})

def cars(request):
    return render(request, 'driver_app/cars.html', {})


def car_reg(request):
    form = CarRegForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Car successfully registered!')
            return redirect('home')
    context = {'form':form}
    return render(request, 'driver_app/car_reg.html', context)

def profile(request):
    return render(request, 'driver_app/profile.html', {})

class StaffView(ListView):
    model = Account
    template_name = 'driver_app/staffview.html'
    paginate_by = 8

class CarView(ListView):
    model = Cars
    paginate_by = 8
    template_name = 'driver_app/carview.html'

    
