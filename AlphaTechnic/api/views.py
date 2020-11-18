# from .models import Post
# from .serializers import PostSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from django.shortcuts import get_object_or_404
#
#
# class PostListAPIView(APIView):
#     def get(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)
#
#
# class PostDetailAPIView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Post, pk=pk)
#
#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import status
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Post
# from .serializers import PostSerializer
# import datetime
#
#
# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     # url : posts/popular/
#     @action(detail=False)
#     def popular(self, request): # 좋아요 20개 이상 받은 인기 posts
#         qs = self.queryset.filter(likes__gt=20).order_by('-posted_date')[:10]
#         serializer = self.get_serializer(qs, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#     # url : posts/today/
#     @action(detail=False)
#     def today(self, request): # 오늘 생성된 posts
#         today = datetime.date.today()
#         qs = self.queryset.filter(posted_date__gt=today).order_by('-posted_date')
#         serializer = self.get_serializer(qs, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#     # url : posts/{pk}/add_likes/
#     @action(detail=True, methods=['get', 'patch'])
#     def add_likes(self, request, pk):  # 좋아요 하나 추가
#         obj = self.get_object()
#         obj.likes += 1
#         obj.save()
#         serializer = self.get_serializer(obj)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#     # url : posts/{pk}/add_dislikes/
#     @action(detail=True, methods=['get', 'patch'])
#     def add_dislikes(self, request, pk):  # 싫어요 하나 추가
#         obj = self.get_object()
#         obj.dislikes += 1
#         obj.save()
#         serializer = self.get_serializer(obj)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)


################# filtering 미션
from django_filters.rest_framework import FilterSet, filters, DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets

from .permissions import IsAuthorOrReadonly
from .models import Post
from .serializers import PostSerializer


class PostFilter(FilterSet):
    content = filters.CharFilter(lookup_expr='icontains') # GET으로 넘어온 string이 content에 포함되는가
    posted_date = DateFromToRangeFilter() # GET으로 넘어온 start 날짜 ~ end 날짜에 posted_date가 포함되는가
    likes = filters.NumberFilter(lookup_expr='gte') # GET으로 넘어온 숫자보다 likes 수가 많은가
    dislikes = filters.BooleanFilter(field_name='malcious', method='malicious_posts', label="malcious")

    class Meta:
        model = Post
        fields = ['content', 'posted_date', 'likes', 'dislikes']

    def malicious_posts(self, queryset, name, value): # dislikes의 수가 15개인데 likes가 3개 이하인 queryset
        filtered_queryset = queryset.filter(dislikes__gte=15).filter(likes__lte=3).order_by('-posted_date')
        return filtered_queryset


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    permission_classes = [
             IsAuthorOrReadonly,
    ]

