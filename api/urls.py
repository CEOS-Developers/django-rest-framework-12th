from django.urls import path, include
from . import views


urlpatterns = [
    path('movie/', views.MovieListAPIView.as_view()),
    #path('movie/', views.movie_list),
    path('movie/<int:pk>/', views.MovieDetailAPIView.as_view()),
    #path('movie/<int:pk>', views.movie_detail),
]