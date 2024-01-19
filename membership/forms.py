from django import forms
from django.db import models
from .models import Membership

class userProfileForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['memberlevel']
