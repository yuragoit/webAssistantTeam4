from django import forms
from .models import Contact
import datetime


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Bob',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '+380661234567',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@gmail.com',
    }), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ukraine, Kiev, Soborna Street 100',
    }), required=False)
    birthday = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }), required=False)

    class Meta:
        model = Contact
        fields = ['first_name', 'phone_number', 'email', 'birthday', 'address']