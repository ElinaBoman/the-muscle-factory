from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import datetime, time


# Create your models here.
# The structure of this model was inspired by gStarHigh, the model has been modified to suit this project. I have created the eventchoices.

class EventBooking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_booking")
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now=True)
    event_date = models.DateField(auto_now=False)
    TIME_INTERVALL = (
        ("08:00",  "08:00"),
        ("09:00", "09:00"),
        ("10:00", "10:00"),
        ("11:00", "11:00"),
        ("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00")
    )
    lesson_time = models.CharField(max_length=10, choices=TIME_INTERVALL)
    
    EVENT_CHOICE = (
        ("Personal Trainer", "Personal Trainer"),
        ("Dietist", "Dietist"),
        ("Rehab", "Rehab"),
        ("Massage", "Massage"),
    )
    event_choice = models.CharField(max_length=30, choices=EVENT_CHOICE)

    BOOKING_STATUS = ((0, "Awaiting Approval"), (1, "Confirmed"))
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    extra_comments = models.TextField(null=True, blank=True, verbose_name='Anything you would like to add?')
   
    star_smiley = "\U0001F929"
    OPTIONS = [
        ('option_yes', 'Yes' + star_smiley),
        ('option_no', 'No'),
    ]

    options_field = models.CharField(max_length=10, choices=OPTIONS, default='option_yes',)
      
    
    class Meta:
        ordering = ["event_date"]

    def __str__(self):
         return f"{self.user} - {self.event_choice}"


