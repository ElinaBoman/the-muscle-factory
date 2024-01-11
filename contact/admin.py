from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ContactForm

# # Register your models here.
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "lastname", "phonenumber","email", "message")
    search_fields = ["name", "email"]
    actions = ['approve_booking']
