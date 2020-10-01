from django.shortcuts import render
from .serializers import UserSerializer, CustomerSerializer, ProductSerializer, ChoiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from .models import Customer, Product, Choice

#post -> 생성, get -> 조회, put -> 수정, delete->삭제
#ListAPIView:모델 객체 목록 및 새로운 객체 생성(get, post)
#DetailAPIView:객체 내용, 수정, 삭제(get, put, delete)
class UserListAPIView(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)#many=True왜쓰지?
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)#POST통한 리소스 생성 작업 성공시
        return Response(serializer.errors, status=400)#클라이언트 요청 부적절 시 사용

from django.shortcuts import get_object_or_404

class UserDetailAPIView(APIView):
    def get_object(self, pk): #이거 왜쓰지..??
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk, format=None):#format옵션 뭐지?
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#이거 status뭐지?

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)#상태코드 이거 뭐임?



