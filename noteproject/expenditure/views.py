from rest_framework import viewsets, permissions


from .models import BankAccount, Expenditure, Income
from .serializers import BankAccountSerializer, ExpenditureSerializer, IncomeSerializer
from .mixins import MarkIsCheckMixin

# filter_backends, search_fields, ordering_fields 를 사용하여 내장된 필터를 활성화 할 수 있다.
# 커스텀 필터 또한 생성 가능
class BankAccountViewSet(viewsets.ModelViewSet):

    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class ExpenditureViewSet(MarkIsCheckMixin, viewsets.ModelViewSet):

    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer

    def create(self, request, *args, **kwargs):
        return self.create_with_bank_account(request, Expenditure, self.get_serializer_class())

class IncomeViewSet(MarkIsCheckMixin, viewsets.ModelViewSet):

    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    
    def create(self, request, *args, **kwargs):
        return self.create_with_bank_account(request, Income, self.get_serializer_class())