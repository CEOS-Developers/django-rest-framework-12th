from django.urls import path, include
from .views import post_api

urlpatterns = [
    path("post/", post_api),
]