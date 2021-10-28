from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def save_user(self, validated_data):
        user = User.objects.create_user( 
                                password=validated_data.get('password'), 
                                email=validated_data.get('email'))
        user.save()
        return user