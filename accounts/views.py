from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework import (mixins, generics, status)
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings


from accounts.serializers import UserSerializer

# Create your views here.

User = get_user_model()

class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # u = User.objects.create_user() #alternate method
        # u.save()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save_user(serializer.data)
            token = Token.objects.get_or_create(user=user)
            send_mail("Confirmation Email from E-Commerce", "Please Confirm your email by clicking the link below\n"+settings.FRONT_END_HOST+'/verify-user/user-id='+str(token[0].key), settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
            return JsonResponse({'status': 'created'}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user=user)
        context = {
            'user_id' : user.pk,
            'email': user.email,
            'token': token.key
        }
        return JsonResponse(context)


# class SignupView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request, format=None):
#         serializer = SignupSerializer(data=request.data)
#         if serializer.is_valid():   #Takes care of validation using params on model.
#             user = serializer.save_user(serializer.data)
#             token = Token.objects.get(user=user)
#             send_mail("NAD: Confirm Email", "Please confirm your email by clicking the link below\n"+settings.FRONT_END_HOST+"/verify-user/user-id="+str(token.key), settings.EMAIL_HOST_USER, [user.email])
#             return JsonResponse({'status': 'created'}, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserInfo(mixins.ListModelMixin, generics.GenericAPIView):

    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        try:
            return User.objects.filter(auth_token=self.kwargs['pk'])
        except:
            raise Http404

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class Verification(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        token = self.kwargs['pk']
        user = User.objects.get(auth_token=token)
        Token.objects.filter(key=token).delete()
        new_token = Token.objects.create(user=user)
        context = {
            'user_id' : user.pk,
            'email': user.email,
            'token': new_token.key
        }
        return JsonResponse(context)