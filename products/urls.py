from django.urls import path
from .views import (
    CategoryItemsList,
    ProductList,
    ProductDetail,
    CategoriesList
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
    path('prod/', ProductList.as_view(), name='Product-List'),
    path('prod/<int:pk>/', ProductDetail.as_view(), name='Product-Detail-View'),
    path('cats/', CategoriesList.as_view(), name='Categories-List'),
    path('cats/<str:pk>/', CategoryItemsList.as_view(), name='Categories-Items-List'),
]