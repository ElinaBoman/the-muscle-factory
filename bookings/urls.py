from django.urls import path
from . import views
from bookings.views import process_form, my_bookings, delete_booking, edit_item

urlpatterns = [
    path('process_form/', process_form, name='process_form'),
    path('my_bookings/', my_bookings, name='my_bookings'),
    path('my_bookings/delete_booking/', delete_booking, name='delete_booking'),
    path('bookings/edit_item/', edit_item, name='edit_item'),
]

