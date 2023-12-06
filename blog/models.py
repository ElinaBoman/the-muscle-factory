from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# This is from I think therefore I blog project with Code Institute
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


# class Comment(models.Model):
#     post = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="comments")
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"

# The diffrent membership levels to choose from.
MEMBERSHIP_LEVELS = (
    ("Brons", "Brons"),
    ("Silver", "Silver"),
    ("Gold", "Gold"),
    )
# This is model is for admin page to manage new members and add correct membership to their name.
class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    memberlevel = models.CharField(max_length=80, choices=MEMBERSHIP_LEVELS, default="Brons")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.name} - {self.memberlevel}"

# Booking system

BOOKING_STATUS = ((0, "Awaiting Approval"), (1, "Confirmed"))

# The structure of this model was inspired by gStarHigh, the model has been modified to suit this project. I have created the eventchoices.
class EventBooking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_eventbookings')
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now=True)
    event_date = models.TimeField(auto_now=False)
    lesson_time = models.TimeField(default="12:30")
    EVENT_CHOICE = (
        ("Personal Trainer", "Personal Trainer"),
        ("Dietist", "Dietist"),
        ("Rehab", "Rehab"),
        ("Massage", "Massage"),
    )
    event_choice = models.CharField(max_length=30, choices=EVENT_CHOICE)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)

    class Meta:
        ordering = ["event_date"]

    def __str__(self):
         return f"{self.user} - {self.event_choice}"


