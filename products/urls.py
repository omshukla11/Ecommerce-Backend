from django.urls import path
from .views import (
    CategoryItemsList,
    CategoryList,
    ProductList,
    ProductDetail,
    CategoriesList,
    SubCategoryList
    # productCreateView,
    # productDetailView,
    # productUpdateView,
    # productView,
)

urlpatterns = [
    path('prod/', ProductList.as_view(), name='Product-List'),
    path('prod/<int:pk>/', ProductDetail.as_view(), name='Product-Detail-View'),
    path('prod/<str:pk>/', CategoryItemsList.as_view(), name='Categories-Items-List'),
    path('cats/', CategoryList, name='Categories-List'),
    path('subcats/', CategoriesList.as_view(), name='Categories-List'),
    path('subcats/<str:pk>/', SubCategoryList.as_view(), name='Sub-Category-List'),
]