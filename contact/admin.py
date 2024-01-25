from django.contrib import admin
from .models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    # Admin can display messages sent with ContactForm
    list_display = ("name", "lastname", "phonenumber", "email", "message")
    search_fields = ["name", "email"]
    actions = ['approve_booking']
