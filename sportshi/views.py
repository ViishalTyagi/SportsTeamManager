from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import views, status, generics
from rest_framework.response import Response
from .serializers import LoginSerializer, SignUpSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from django.db.models import Q

User = get_user_model()

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class LoginView(views.APIView):
    serializer_class=LoginSerializer
    permission_classes=[AllowAny]
    def post(self, request, *args, **kwargs):
        #print(request.user)
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username') # username or email address
        password = data.get('password')
        qs = User.objects.filter(
                Q(username__iexact=username)|
                Q(email__iexact=username)
            ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                # JWT Auth can be used once Debug=False is set in settings along with other changes:
                # payload = jwt_payload_handler(user)
                # token = jwt_encode_handler(payload)
                # response = jwt_response_payload_handler(token, user, request=request)
                return Response({'data': data})
        return Response({"detail": "Invalid credentials"}, status=401)