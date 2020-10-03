from django.urls import path, include
from .views import post_api, selected_post_api

urlpatterns = [
    path("post/", post_api),
    path("post/<int:pk>/", selected_post_api)
]