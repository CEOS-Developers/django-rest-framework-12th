from django.shortcuts import render
from .serializers import MovieSerializer
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .models import Comment
from django.http import Http404

class MovieList(APIView):
    #영화 리스트 조회
    def get(self, request, format=None):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        json_data = serializer.data
        return Response(json_data)

    #영화 생성
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#serializer에서 request.date 만 받아오면 새로운 데이터를 저장한다는 것,
#queryset(원래 있던 데이터)까지 받아오면 수정을 한다는 것

class MovieDetail(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    #특정 영화 조회
    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    #특정 영화 리스트 수정
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = MovieSerializer(queryset, data=request.data)
        #리스트 수정할때 genre 는 model 안 장르 choiceset 안의 장르만 입력해야하는데 이게 모델때문인지 is_valid 때문인지
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #특정 영화 정보 삭제
    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentList(APIView):
    #comment 조회
    def get(self, request, format=None):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        json_data = serializer.data
        return Response(json_data)

    #comment 생성
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    #특정 코멘트 조회
    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = MovieSerializer(comment)
        return Response(serializer.data)

    #특정 코멘트 수정
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = CommentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #특정 코멘트 삭제
    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)