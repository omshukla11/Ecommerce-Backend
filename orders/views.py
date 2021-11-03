from django.shortcuts import render
from rest_framework import ( mixins, generics )

from orders.models import Order
from orders.serializers import OrderSerializer, PlaceOrderSerializer


# Create your views here.

class OrderList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PlaceOrder(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = PlaceOrderSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)