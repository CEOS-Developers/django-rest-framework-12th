from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie, Profile
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


# 영화 목록 및 새 영화 생성
class MovieListAPIView(APIView):
    def get(self, request):
        serializer = MovieSerializer(Movie.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


'''
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        query_set = Movie.objects.all()
        serializer = MovieSerializer(query_set, many=True)
        return Response(serializer.data)
    else:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
'''


# 영화 내용, 수정, 삭제
class MovieDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Movie, pk=pk)

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = MovieSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''