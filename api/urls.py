from django.urls import path
from . import views
from rest_framework import routers

# CBV url patterns
urlpatterns = [
    path('routine/', views.RoutineList.as_view()),
    path('routine/<int:pk>/', views.RoutineDetail.as_view())
]

