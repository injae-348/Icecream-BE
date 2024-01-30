from django.contrib import admin
from .models import BankAccount, Expenditure, Income

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('userId','name', 'balance')
    search_fields = ('name', 'userId__username')

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('date', 'tag', 'price', 'content', 'contain', 'bankAccountId')
    search_fields = ('tag', 'content', 'bankAccountId__name')  # 'bankAccountId'는 ForeignKey로 연결된 BankAccount 모델의 name을 검색할 수 있도록 추가

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'tag', 'price', 'content', 'contain', 'bankAccountId')
    search_fields = ('tag', 'content', 'bankAccountId__name')  # 'bankAccountId'는 ForeignKey로 연결된 BankAccount 모델의 name을 검색할 수 있도록 추가
    