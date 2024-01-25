from django import forms
from django.utils import timezone
import datetime
from .models import EventBooking
import datetime as dt
from django.forms import Select


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        '''
        This will take todays date in a isoformat,
        splits to only use the part before the T.
        Set min value for dates inside widgets, event_date.
        '''
        min_date = (timezone.localdate())
        iso_string = min_date.isoformat()
        iso_split_date = iso_string.split("T")[0]

        '''
        HOUR_CHOICES will show avaible times in a select box.
        Credits to tutor John at Code Institute, who helped me create code.
        '''
        HOUER_CHOICES = [
                (dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 18)]

        fields = [
            'event_date',
            'start_time',
            'event_choice',
            'options_field',
            'extra_comments'
        ]

        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date',
                                                 'min': iso_split_date}),
            'options_field': forms.RadioSelect(),
            'start_time': Select(choices=HOUER_CHOICES),
        }

        labels = {
            'options_field': 'Is this your first appointment?',
        }
