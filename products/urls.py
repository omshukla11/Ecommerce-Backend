from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
    # productCreateView,
    # productDetailView,
    # productUpdateView,
    # productView,
)

# urlpatterns = [
#     path('task/', productView, name='Product-List'),
#     path('task/<int:pk>/', productDetailView, name='Product-Detail-View'),
#     path('create/', productCreateView, name='Create-Product'),
#     path('update/<int:pk>/', productUpdateView, name='Update-Product'),
# ]

urlpatterns = [
    path('task/', ProductList.as_view(), name='Product-List'),
    path('task/<int:pk>/', ProductDetail.as_view(), name='Product-Detail-View')
]