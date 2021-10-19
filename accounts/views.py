from django.shortcuts import render
from rest_framework import (mixins, generics)
from django.contrib.auth import get_user_model

from accounts.serializers import UserSerializer

# Create your views here.

User = get_user_model()

class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)