from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import UserDetailAPIView, UserListAPIView
from . import views

urlpatterns = [
    path('users/', views.UserListAPIView.as_view()),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)


