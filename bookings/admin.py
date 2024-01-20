from django.contrib import admin
from .models import EventBooking

# # Register your models here.
@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = ("user", "event_date", "start_time","event_choice", "extra_comments", "options_field", "booking_status")
    list_filter = ('booking_status', 'created_on')
    search_fields = ["user", "event_date", "booking_status"]
    actions = ['approve_booking']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
