from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Product(models.Model):
    Cats = (
        ('Elec', 'Electronics'),
        ('MCol', "Men's Fashion"),
        ('FCol', "Women's Fashion"),
    )
    name        = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10)
    featured    = models.BooleanField(blank=False)
    instock     = models.IntegerField()
    category    = models.CharField(max_length=4, choices=Cats, blank=True)
    product_img = models.ImageField(default='default.jpg', upload_to='image/')

    def __str__(self):
        return self.name