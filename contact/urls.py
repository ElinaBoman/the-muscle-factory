from . import views
from django.shortcuts import render, HttpResponse
from django.urls import path, include
from .views import contact

urlpatterns = [
    path('contact/', contact, name='contact'),
]