from django.contrib import admin

from orders.models import Order, QuantProd

# Register your models here.

admin.site.register(QuantProd)
admin.site.register(Order)

