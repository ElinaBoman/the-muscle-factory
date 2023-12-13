from django.contrib import admin
from .models import EventBooking

# # Register your models here.
@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = ("user", "event_date", "lesson_time","event_choice", "booking_status")
    list_filter = ('booking_status', 'created_on')
    search_fields = ("user", "event_date", "booking_status")
