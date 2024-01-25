from . import views
from django.urls import path
from .views import about

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path('about/', about, name="about"),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]
