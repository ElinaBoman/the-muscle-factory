from django.urls import path
from . import views
from bookings.views import process_form, my_bookings

urlpatterns = [
    path('process_form/', process_form, name='process_form'),
    path('my_bookings/', my_bookings, name='my_bookings'),
]