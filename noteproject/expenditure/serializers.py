from rest_framework import serializers
from .models import BankAccount, Expenditure, Income

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['id','userId','name','balance']

class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = ['id','date','tag','price','content','contain','bankAccountId']

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id','date','tag','price','content','contain','bankAccountId']