from . import views
from django.shortcuts import render, HttpResponse
from django.urls import path, include
from .views import userProfile_view

urlpatterns = [
    path('membership/', userProfile_view, name='membership'),
]