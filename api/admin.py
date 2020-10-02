from django.contrib import admin

from .models import Customer, Product, Choice

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'addr', 'membership']#Admin 목록에 보여질 필드 목록

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'quantity']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'price', 'color', 'size']
