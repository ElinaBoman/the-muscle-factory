from django import forms
from django.utils import timezone
import datetime
from django.db import models
from .models import EventBooking

'''
This class will create the structure of the form.

'''
class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        '''
        This will take todays date in a isoformat that we split to only use the part before the T.
        This we can later use to set min value for dates inside widgets, event_date.
        Because the iso_split_date itself is a string I do not use the quotes.
        '''
        min_date = (timezone.localdate())
        iso_string = min_date.isoformat()
        iso_split_date = iso_string.split("T")[0]
        '''
        bookable_times will show the user what times that are aviable to book.
        
        bookable_times = [
            (f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}")
            for hour in range(9, 17) for minute in (0, 30)
        ]
        '''
        fields = ['event_date', 'lesson_time', 'event_choice', 'options_field', 'extra_comments']
        widgets = {
        'event_date':forms.DateInput(attrs={'type':'date', 'min': iso_split_date}),
        'options_field': forms.RadioSelect(),
        }

        labels = {
            'options_field': 'Is this your first appointment?',
        }






