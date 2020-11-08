from django.contrib import admin

from .models import Customer, Product, Choice, Category, Cart

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'addr', 'membership']#Admin 목록에 보여질 필드 목록

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'price', 'color', 'size']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_quantity', 'total_payment']