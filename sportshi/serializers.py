from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers, exceptions

User = get_user_model()

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True} }

