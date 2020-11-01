######### <각 클래스에 대해 as_view로 라우팅>
# from django.urls import path, include
# from rest_framework.response import Response
# from .models import Post
# from . import views

# urlpatterns = [
#     # 각 클래스에 대해 as_view로 라우팅
#     path('api/posts/', views.PostListAPIView.as_view()),
#     path('api/posts/<int:pk>/', views.PostDetailAPIView.as_view()),
# ]


# ######### <Notion 학습 Router>
# from rest_framework import routers
# from .views import PostViewSet
#
# router = routers.DefaultRouter()
# router.register()

from rest_framework.decorators import action
from rest_framework import viewsets, status, serializers


# class PostViewSet(viewsets.ModelViewSet):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#     @action(methods=['get'], detail=False, url_name='method', url_path='method')
#     def method(self, request, *args, **kwargs):
#         return Response(status=status.HTTP_200_OK, data=serializers.data)

######### <최종 Router 사용>
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
