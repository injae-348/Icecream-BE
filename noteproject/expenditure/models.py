from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel,CostModel

# 어디 계좌인지 혹은 현금인지 name에 작성
class BankAccount(TimeStampedModel):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Expenditure(CostModel):
    bankAccountId = models.ForeignKey(BankAccount,on_delete=models.CASCADE)


class Income(CostModel):    
    bankAccountId = models.ForeignKey(BankAccount,on_delete=models.CASCADE)
