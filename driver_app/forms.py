from cProfile import Profile
from django import forms
from .models import Cars, Payment
from accounts.models import Account



class CarRegForm(forms.ModelForm):
    type = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': ' Car Type'}))
    date = forms.DateField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Date Purchased'}))
    number_Plate = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Number Plate'}))
    cost = forms.FloatField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Cost of car'}))
   


    class Meta:
        model = Cars
        fields = ('type', 'date', 'number_Plate', 'cost')

class CarSearchForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['type']

class UpdateUserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'input your email'}))
    Profile = forms.ImageField(widget=forms.FileInput())
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'input new password'}))
    Confirm_Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm new password'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'input your address'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'input your phone number'}))

    class Meta:
        model = Account
        fields = ('name', 'email', 'Profile', 'Password', 'Confirm_Password', 'address', 'phone_number')

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ('driver', 'payment_made', 'balance', 'date_of_payment', 'status')

