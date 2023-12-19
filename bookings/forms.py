from django import forms

from django.core.validators import MaxValueValidator
from django.utils import timezone
import datetime
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
        '''
        This will take todays date in a isoformat that we split to only use the part before the T.
        This we can later use to set min value for dates inside widgets, event_date.
        Because the iso_split_date itself is a string I do not use the quotes.
        '''
        min_date = (timezone.localdate())
        iso_string = min_date.isoformat()
        iso_split_date = iso_string.split("T")[0]
        fields = ['event_date', 'lesson_time', 'event_choice']
        widgets = {
            'event_date':forms.DateInput(attrs={'type':'date', 'min': iso_split_date}),
            'lesson_time':forms.Select(choices=bookable_times),
        }
