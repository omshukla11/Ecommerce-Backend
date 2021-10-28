from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import (mixins, generics, status)
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


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
            return JsonResponse({'status': 'created', 'token': str(token[0].key) }, status=status.HTTP_201_CREATED)
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