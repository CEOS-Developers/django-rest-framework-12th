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


import django_filters
from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend

class ProductFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter()
    price = django_filters.NumberFilter()
    color = django_filters.CharFilter(method='my_custom_color')

    """
    #밑의 Meta class의 fields 속성과 동일한 역할
    category = django_filters.NumberFilter(field_name='category', lookup_expr='exact')
    price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    """
    class Meta:
        model = Product
        fields = {
            'price' : ['lte'], #generate 'price__lte' filters
            'color' : ['iexact'] #generate 'color__iexact' filters
        }

    def my_custom_color(self, queryset, name, value):
        """
        #construct the full lookup expression
        lookup = '__'.join([name, 'iexact'])
        return queryset.filter(**{lookup: 'orange'})
        """
        return queryset.filter(**{name: 'black'}) #다른 색깔 입력해도 왜 black 객체만 나오지..?

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

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

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

