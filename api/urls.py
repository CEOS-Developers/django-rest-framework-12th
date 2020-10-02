from django.urls import path, include
from . import views


urlpatterns = [
    path('movie/', views.MovieListAPIView.as_view()),
    path('movie/<int:pk>/', views.MovieDetailAPIView.as_view()),
    path('profile/', views.ProfileListAPIView.as_view()),
    path('profile/<int:pk>/', views.ProfileDetailAPIView.as_view()),
]