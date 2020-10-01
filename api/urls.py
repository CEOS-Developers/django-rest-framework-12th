from django.urls import path
from . import views

urlpatterns = [
    path('routine/', views.RoutineList.as_view()),
    path('routine/<int:pk>/', views.RoutineDetail.as_view())
]