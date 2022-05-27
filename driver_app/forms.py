from django import forms
from .models import Cars


class CarRegForm(forms.ModelForm):
    type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Car Type'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Date Purchased'}))
    number_Plate = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Number Plate'}))
    cost = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Cost of car'}))
   


    class Meta:
        model = Cars
        fields = ('type', 'date', 'number_plate', 'cost')

class CarSearchForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['type']


