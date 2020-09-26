from django.db import models
from posts.models import Product


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=255,blank=True)
    data_added = models.DateField(auto_now_add=True)  # 구입 상품 별 날짜

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    number = models.IntegerField()

    def total(self):
        return self.product.price * self.number

    def __str__(self):
        return self.product