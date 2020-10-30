from django.shortcuts import render
from .serializers import UserSerializer, CustomerSerializer, ProductSerializer, ChoiceSerializer, CartSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from .models import Customer, Product, Choice, Cart, Category
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

#post -> 생성, get -> 조회, put -> 수정, delete->삭제
#ListAPIView:모델 객체 목록 조회 및 새로운 객체 생성(get, post) -> 목록에 대한
#DetailAPIView:객체 내용, 수정, 삭제(get, put, delete) -> 특정 객체에 대한 

#ModelViewSet: list, create, retrieve, update, destroy actions 제공

#User
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


#Customer
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

#product
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

#Category
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

#choice
class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

#Cart
class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
