from . import views
from django.urls import path
from .views import about, contact

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]