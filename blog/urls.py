from . import views
from django.urls import path
from .views import about

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
     path('about/', about, name="about"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]