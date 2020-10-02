from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import UserDetailAPIView, UserListAPIView
from . import views

urlpatterns = [
    path('users/', views.UserListAPIView.as_view()),
    path('users/<int:pk>/', views.UserDetailAPIView.as_view()),
    path('customers/', views.CustomerListAPIView.as_view()),
    path('customers/<int:pk>/', views.CustomerDetailAPIView.as_view()),
    path('products/', views.ProductListAPIView.as_view()),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('choices/', views.ChoiceListAPIView.as_view()),
    path('choices/<int:pk>/', views.ChoiceDetailAPIView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)


