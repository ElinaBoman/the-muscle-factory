from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
# The structure of this model was inspired by gStarHigh, the model has been modified to suit this project. I have created the eventchoices.

class EventBooking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_booking")
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now=True)
    event_date = models.DateField(auto_now=False)
    lesson_time = models.TimeField(default="08:00")

    EVENT_CHOICE = (
        ("Personal Trainer", "Personal Trainer"),
        ("Dietist", "Dietist"),
        ("Rehab", "Rehab"),
        ("Massage", "Massage"),
    )
    event_choice = models.CharField(max_length=30, choices=EVENT_CHOICE)

    BOOKING_STATUS = ((0, "Awaiting Approval"), (1, "Confirmed"))
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    extra_comments = models.TextField(null=True)
    smiley_happy = "\U0001F604"
    star_smiley = "\U0001F929"
    option_yes = models.BooleanField(default=False, verbose_name='This is my first appointment!' + star_smiley)
    option_no = models.BooleanField(default=False, verbose_name="I'm a recurring member!" + smiley_happy)
    
    class Meta:
        ordering = ["event_date"]

    def __str__(self):
         return f"{self.user} - {self.event_choice}"


