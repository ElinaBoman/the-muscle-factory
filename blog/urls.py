from . import views
from django.shortcuts import render, HttpResponse
from django.urls import path, include
from .views import about, EventList, EventDetail

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path('about/', about, name="about"),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    
]