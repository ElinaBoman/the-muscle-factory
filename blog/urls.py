from . import views
from django.urls import path
from .views import about, contact

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]