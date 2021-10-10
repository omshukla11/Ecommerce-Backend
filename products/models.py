from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.



class Product(models.Model):
    Cats = (
        ('Elec', 'Electronics'),
        ('Fash', 'Fashion'),
    )
    name        = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=6)
    sold        = models.BooleanField(default=False)
    featured    = models.BooleanField(blank=False)
    soldon      = models.DateTimeField()
    instock     = models.IntegerField()
    category    = models.CharField(max_length=4, choices=Cats, blank=True)

    def __str__(self):
        return self.name