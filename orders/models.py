from django.contrib.auth.models import User
from django.db import models

from shop.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey('shop.Product', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
