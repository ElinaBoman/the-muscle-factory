from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# This is from I think therefore I blog project with Code Institute. This will only be used by admin, to create events.
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

