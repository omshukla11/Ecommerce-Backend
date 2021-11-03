from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class QuantProd(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True)

class Order(models.Model):
    products = models.ManyToManyField(QuantProd)
    order_by = models.ForeignKey(User, on_delete=models.CASCADE)