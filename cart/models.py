from django.db import models
from posts.models import Product


# Create your models here.
class Cart(models.Model):
    data_added = models.DateField(auto_now_add=True, verbose_name="cart_date")


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item_date")
    number = models.IntegerField()

    def total(self):
        return self.product.price * self.number

    def __str__(self):
        return self.product