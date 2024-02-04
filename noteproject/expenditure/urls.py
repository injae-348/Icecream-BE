from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'account',views.BankAccountViewSet)

urlpatterns = [
    path('',include(router.urls)),
]

# GET   /v1/api/account     BankAccount 리스트
# POST  /v1/api/account     BankAccount 생성

# GET   /v1/api/account/pk  BankAccount 세부 사항(pk에 해당하는 1개)
# PUT, PATCH 내용 업데이트
# DELETE 삭제