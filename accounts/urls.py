from django.urls import path
from .views import CustToken, UserInfo, UserList, Verification
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', UserList.as_view(), name='User-List'),
    path('users/login-token/', CustToken.as_view(), name='Auth-Token'),
    path('users/info/<str:pk>/', UserInfo.as_view(), name='User-Info'),
    path('users/verify/<str:pk>/', Verification.as_view(), name='User-Info'),
]