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
        
        min_date = (timezone.localdate())
        iso_string = min_date.isoformat()
        iso_split_date = iso_string.split("T")[0]
        fields = ['event_date', 'lesson_time', 'event_choice']
        widgets = {
            'event_date':forms.DateInput(attrs={'type':'date', 'min': iso_split_date}),
            'lesson_time':forms.Select(choices=bookable_times),
        }
        

#     # Skapa ett datetime-objekt för nuvarande datum och tid
# current_datetime = datetime.now()

# # Använd isoformat för att få strängrepresentationen i ISO 8601-format
# iso_formatted_string = current_datetime.isoformat()

# # Extrahera bara datumdelen
# iso_date_only = iso_formatted_string.split("T")[0]


        '''
        DOM restaurants
        '''

        # if event_date < timezone.localdate():
        #     raise ValidationError('Sorry you have to book a future date')

   
    



        # def validate_date(self):
        #     if event_date < timezone.localdate():
        #         raise ValidationError('Date invalid')
        #     return event_date
 
        





