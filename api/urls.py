from django.urls import path, include
from .views import post_api, selected_post_api, create_post_api

urlpatterns = [
    path("post/", post_api),
    path("post/<int:pk>/", selected_post_api),
    path("items/", create_post_api)
]