from django.db import models


class ContactForm(models.Model):
    '''
    Contact form model.
    '''
    name = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    phonenumber = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)


    class Meta:
        ordering = ["email"]

    def __str__(self):
         return f"{self.name} - {self.email}"