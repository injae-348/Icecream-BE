from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from .models import BankAccount, Expenditure, Income
from .serializers import BankAccountSerializer, ExpenditureSerializer, IncomeSerializer
from .mixins import MarkIsCheckMixin

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class ExpenditureViewSet(MarkIsCheckMixin, viewsets.ModelViewSet):
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer


class IncomeViewSet(MarkIsCheckMixin, viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
