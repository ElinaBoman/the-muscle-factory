from django.db import models

# Create your models here.


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