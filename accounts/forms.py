from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account, UserProfile





class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email'}), help_text='Required. Add a valid email address')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'address'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'phone_number'}))
    car = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'car'}))
    details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'details'}))


    class Meta:
        model = Account
        fields = ('email', 'username', 'address', 'phone_number', 'car', 'details')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'avatar')

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        return avatar
