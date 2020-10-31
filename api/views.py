from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from .models import *
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

    #url : api/products/{pk}/category -> pk는 category_id
    @action(methods=['get'], detail=True)
    def category(self, request, pk):
        products = Product.objects.all().filter(category=pk)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

#Category
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


    #다시보기...
    #url : api/categories/{pk}/product/ -> 해당 카테고리 이름과 해당 카테고리의 상품들 나오게
    #get_serializer_class 함수 재정의 -> 함수 역할: return the class to use for the serializer
"""
    def get_serializer_class(self):
        if self.action == 'retrieve':
            p = ProductViewSet
            return p.serializer_class
"""
#Cart
class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

#choice
class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

    #url : api/choices/{pk}/customer -> pk는 customer_id
    @action(methods=['get'], detail=True)
    def customer(self, request, pk):
        choices = Choice.objects.filter(customer_id=pk)
        serializer = self.get_serializer(choices, many=True)
        return Response(serializer.data)

