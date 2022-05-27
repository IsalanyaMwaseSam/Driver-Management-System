from django.contrib.auth.models import User
import email
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully registered!')
            return redirect('home')
        else:
            messages.error(request, 'Passwords Dont Match')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form} )

def login(request):
    if request.method == 'POST':
            username = username.POST['username']
            password = request.POST['password']

            try:
                user = Account.objects.get(username=username)
            except:
                messages.error(request, 'username does not exist')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username Or Password')
    return render(request, 'accounts/login.html', {} )
