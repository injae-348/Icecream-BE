from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from . import views


urlpatterns = [
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('register/',views.RegisterAPIView.as_view()),
    path('auth/',views.AuthAPIView.as_view()),
]

# GET       auth/ 유저 정보 가져오기
# POST      auth/ 로그인
# DELETE    auth/ 로그아웃