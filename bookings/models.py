from django.db import models
import uuid
from django.contrib.auth.models import User
import datetime


# Create your models here.
# The structure of this model was inspired by gStarHigh, the model has been modified to suit this project. I have created the eventchoices.

class EventBooking(models.Model):
    EVENT_CHOICE = (
            ("Personal Trainer", "Personal Trainer"),
            ("Dietist", "Dietist"),
            ("Rehab", "Rehab"),
            ("Massage", "Massage"),
        )
    
    star_smiley = "\U0001F929"
    OPTIONS = [
        ('option_yes', 'Yes' + star_smiley),
        ('option_no', 'No'),
    ]
    BOOKING_STATUS = ((0, "Awaiting Approval"), (1, "Confirmed"))

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_booking")
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now=True)
    event_date = models.DateField(auto_now=False)
    start_time = models.TimeField(default=datetime.time(8, 0))
    event_choice = models.CharField(max_length=30, choices=EVENT_CHOICE)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    extra_comments = models.TextField(null=True, blank=True, verbose_name='Anything you would like to add?')
    options_field = models.CharField(max_length=10, choices=OPTIONS, default='option_yes',)
    
    
    class Meta:
        ordering = ["event_date"]

    def __str__(self):
         return f"{self.user} - {self.event_choice}"


