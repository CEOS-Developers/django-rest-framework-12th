from django.db import models
from api import models as user_model
from posts.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        user_model.User,
        null=True,
        on_delete=models.CASCADE,
    )
    name = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(verbose_name='결제금액')
    order_date = models.DateTimeField(auto_now_add=True)
