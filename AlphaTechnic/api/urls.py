from django.urls import path
from . import views

urlpatterns = [
    # 각 클래스에 대해 as_view로 라우팅
    path('api/posts/', views.PostListAPIView.as_view()),
    path('api/posts/<int:pk>/', views.PostDetailAPIView.as_view()),
]

# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('post', views.PostViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]