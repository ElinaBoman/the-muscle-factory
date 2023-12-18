from django import forms

from django.core.validators import MaxValueValidator
from django.utils import timezone
from datetime import time
from django.db.models import Sum
from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .models import EventBooking

'''
This class will create the structure of the form.
bookable_times will show the user what times that are aviable to book.
'''
class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        bookable_times = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d} AM")
        for hour in range(7, 17) for minute in (0, 30)
        ]
        fields = ['event_date', 'lesson_time', 'event_choice']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'lesson_time': forms.Select(choices=bookable_times),
        }





