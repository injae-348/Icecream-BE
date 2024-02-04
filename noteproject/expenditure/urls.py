from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'account',views.BankAccountViewSet,basename='bankaccount')
router.register(r'expenditure',views.ExpenditureViewSet,basename='expenditure')
router.register(r'income',views.IncomeViewSet,basename='income')

urlpatterns = [
    path('',include(router.urls)),
]

#=======================================================
# GET           /v1/api/account/     BankAccount 리스트
# POST          /v1/api/account/     BankAccount 생성

# GET           /v1/api/account/pk/  BankAccount 세부 사항(pk에 해당하는 1개)
# PUT, PATCH    /v1/api/account/pk/  내용 업데이트
# DELETE        /v1/api/account/pk/  삭제

#=======================================================
# GET           /v1/api/expenditure/         Expenditure 리스트
# POST          /v1/api/expenditure/         생성

# GET           /v1/api/expenditure/pk/      Expenditure 세부 사항(pk에 해당하는 1개)
# PUT, PATCH    /v1/api/expenditure/pk/      내용 업데이트
# DELETE        /v1/api/expenditure/pk/      삭제

# POST          /v1/api/expenditure/pk/mark_is_check/   bool 값의 변경
#                          ㄴ basename이 expenditure으로 지정되어있음

#=======================================================
# GET           /v1/api/income/         Income 리스트
# POST          /v1/api/income/         생성

# GET           /v1/api/income/pk/      Income 세부 사항(pk에 해당하는 1개)
# PUT, PATCH    /v1/api/income/pk/      내용 업데이트
# DELETE        /v1/api/income/pk/      삭제

# POST          /v1/api/income/pk/mark_is_check/   bool 값의 변경
#                          ㄴ basename이 income으로 지정되어있음