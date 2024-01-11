from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)


    class Meta:
        ordering = ["email"]

    def __str__(self):
         return f"{self.name} - {self.email}"