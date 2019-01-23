from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import views
from rest_framework.response import Response
from .serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()


class LoginView(views.APIView):
    serializer_class=LoginSerializer
    permission_classes=[AllowAny]

    #generating token through signal
    
    # def post(self, request, *args, **kwargs):
        # serializer = self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']
        # token, created = Token.objects.get_or_create(user=user)
        # user_serializer = UserSerializer(user)
        # return Response({'token': token.key, 'user': user_serializer.data})
