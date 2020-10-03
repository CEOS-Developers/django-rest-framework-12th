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
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
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


#Customer
class CustomerListAPIView(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CustomerDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Customer, pk=pk)

    def get(self, request, pk, format=None):#format옵션 뭐지?
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#이거 status뭐지?

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)#상태코드 이거 뭐임?

#product
class ProductListAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)#POST통한 리소스 생성 작업 성공시
        return Response(serializer.errors, status=400)#클라이언트 요청 부적절 시 사용


class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#choice
class ChoiceListAPIView(APIView):
    def get(self, request, format=None):
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ChoiceDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Choice, pk=pk)

    def get(self, request, pk, format=None):
        choice = self.get_object(pk)
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)

    def put(self, request, pk):
        choice = self.get_object(pk)
        serializer = ChoiceSerializer(choice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        choice = self.get_object(pk)
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)