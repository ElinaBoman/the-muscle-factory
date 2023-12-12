from django import forms
from .models import EventBooking
from django.core.validators import MaxValueValidator
from django.utils import timezone
from datetime import time
from django.db.models import Sum
from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields = ['event_date', 'lesson_time', 'event_choice']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'lesson_time': forms.TimeInput(attrs={'type': 'time'}),
        }





