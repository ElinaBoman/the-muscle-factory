from django import forms
from django.db import models
from .models import ContactForm




class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'lastname', 'phonenumber', 'email', 'message']
