from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes=[AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    permission_classes=[AllowAny]
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"Token":token.key},status=status.HTTP_200_OK)
    
class LogoutView(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        response = super().post(request,*args,**kwargs)

        if response.status_code == 200:
            try:
                token = Token.objects.get(user=request.user)
                token.delete()
            except Token.DoesNotExist:
                return Response({'Error':'로그인 상태가 아닙니다.'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'정상적으로 로그아웃 되었습니다.'},status=status.HTTP_200_OK)