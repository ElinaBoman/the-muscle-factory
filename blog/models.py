from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# This is for publishing events created in admin panel

STATUS = ((0, "Draft"), (1, "Published"))

'''
This code is from "I think therefore I blog project
 with Code Institute":
https://github.com/Code-Institute-Solutions/Django3blog/tree/master/11_messages/blog
This is the model for creating avents posted
in index.html.
'''


class Event(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True
    )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="blog_posts"
    )
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
    