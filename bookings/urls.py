from django.urls import path
from .views import process_form, my_bookings, delete_booking, edit_item


urlpatterns = [
    path('process_form/', process_form, name='process_form'),
    path('my_bookings/', my_bookings, name='my_bookings'),
    path('my_bookings/delete_booking/<booking_id>',
         delete_booking, name='delete_booking'),
    path('my_bookings/edit_item/<booking_id>/', edit_item, name='edit_item'),
]
