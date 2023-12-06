from django.urls import path
from . import views
from .views import create_booking

urlpatterns = [
    path('create_booking/', create_booking, name='create_booking'),
]