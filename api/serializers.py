from django.contrib.auth.models import User
from .models import Customer, Product, Choice
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'addr', 'membership')

class UserSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()#1대1관계인 customerserializer 추가

    class Meta:
        model = User
        fields = ('id', 'username', 'addr', 'membership')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = "__all__"#모든 필드 serialize










