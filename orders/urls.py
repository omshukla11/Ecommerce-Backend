from django.urls import path

from orders.views import OrderList, PlaceOrder

urlpatterns = [
    path('orders/', OrderList.as_view(), name='Order List'),
    path('placeorder/', PlaceOrder.as_view(), name='Order List'),
]