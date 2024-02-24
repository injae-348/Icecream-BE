from rest_framework import viewsets, permissions


from .models import BankAccount, Expenditure, Income
from .serializers import BankAccountSerializer, ExpenditureSerializer, IncomeSerializer
from .mixins import MarkIsCheckMixin

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