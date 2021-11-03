from rest_framework import serializers
from .models import QuantProd, Order

class QuantProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantProd
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    products = QuantProdSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['products', 'order_by']

class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'