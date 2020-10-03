from django.urls import path

from . import views

urlpatterns = [
    path('', views.BasicView, name='BasicView'),
    path('movielist', views.MovieListView, name='MovieList'),
    path('comment', views.CommentsView, name='comments'),
    path('desc', views.DescriptionView, name='desc')
]