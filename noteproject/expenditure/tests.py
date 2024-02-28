from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import BankAccount, Expenditure
from .serializers import BankAccountSerializer, ExpenditureSerializer

class BankAccountTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(username='test_user')
        self.user_id = self.user.id
        self.bankData = {
            'userId':self.user, # User 모델의 instance 필요
            'name':'NH',
            'balance':10000,
        }
        self.bankAccount = BankAccount.objects.create(**self.bankData)

    def test_get_all_bank_accounts(self):
        response = self.client.get('/v1/api/account/')
        bankAccounts = BankAccount.objects.all()
        serializer = BankAccountSerializer(bankAccounts,many=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['results'],serializer.data)

    def test_get_bank_account(self):
        response = self.client.get(f'/v1/api/account/{self.bankAccount.id}/')
        bankAccount = BankAccount.objects.get(id=self.bankAccount.id)
        serializer = BankAccountSerializer(bankAccount)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)

    def test_create_bank_account(self):
        # 사용자 정보가 아닌 사용자 id를 데이터에 넣어줌
        bank_data = {
            'userId': self.user.id,
            'name': 'NH',
            'balance': 10000,
        }
        response = self.client.post('/v1/api/account/',data=bank_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BankAccount.objects.count(),2)

    def test_update_bank_account(self):
        updated_data = {
            'userId':self.user.id,
            'name':'Kakao Bank',
            'balance':10000
        }
        response = self.client.put(f'/v1/api/account/{self.bankAccount.id}/',data=updated_data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        updated_bank_account = BankAccount.objects.get(id=self.bankAccount.id)
        self.assertEqual(updated_bank_account.userId,self.user)
        self.assertEqual(updated_bank_account.name,updated_data['name'])
        self.assertEqual(updated_bank_account.balance,updated_data['balance'])
        # self.assertEqual(updated_bank_account.publication_date.strftime('%Y-%m-%d'), updated_data['publication_date'])
        # self.assertEqual(str(updated_bank_account.price), updated_data['price'])  # Convert Decimal to string

    def test_delete_bank_account(self):
        response = self.client.delete(f'/v1/api/account/{self.bankAccount.id}/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(BankAccount.objects.count(),0)


# Expenditure랑 Income에 대한 Test Code도 만들기 => 둘중 한개만 해도 됨
class ExpenditureTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # BankAccount 생성
        self.bankAccount = BankAccount.objects.create(
            userId=User.objects.create(username='test_user'),
            name='Test Bank',
            balance=50000,
        )

        self.expenditureData = {
            'bankAccountId':self.bankAccount, # BankAccount Instance
            'date':'2024-02-28',
            'tag':'배달',
            'price':10000,
            'content':'알통떡강정',
            'contain':True,
        }

        self.expenditure = Expenditure.objects.create(**self.expenditureData)

    def test_get_all_expenditures(self):
        response = self.client.get('/v1/api/expenditure/')
        expenditures = Expenditure.objects.all()
        serializer = ExpenditureSerializer(expenditures,many=True)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['results'],serializer.data)

    def test_get_expenditure(self):
        response = self.client.get(f'/v1/api/expenditure/{self.expenditure.id}/')
        expenditure = Expenditure.objects.get(id=self.expenditure.id)
        serializer = ExpenditureSerializer(expenditure)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,serializer.data)

    def test_create_expenditure(self):
        expenditure_data = {
            'bankAccountId':self.bankAccount.id,
            'date':'2024-02-27',
            'tag':'여가',
            'price':14000,
            'content':'귀멸의 칼날',
            'contain':True,
        }
        response = self.client.post('/v1/api/expenditure/',data=expenditure_data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Expenditure.objects.count(),2)

    def test_update_expenditure(self):
        updated_data = {
            'bankAccountId':self.bankAccount.id,
            'date':'2024-02-24',
            'tag':'여가',
            'price':14000,
            'content':'명탐정 코난',
            'contain':True,
        }
        response = self.client.put(f'/v1/api/expenditure/{self.expenditure.id}/',data=updated_data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        updated_expenditure = Expenditure.objects.get(id=self.expenditure.id)
        self.assertEqual(updated_expenditure.bankAccountId,self.bankAccount)
        self.assertEqual(updated_expenditure.date.strftime('%Y-%m-%d'),updated_data['date'])
        self.assertEqual(updated_expenditure.tag,updated_data['tag'])
        self.assertEqual(updated_expenditure.price,updated_data['price'])
        self.assertEqual(updated_expenditure.content,updated_data['content'])
        self.assertEqual(updated_expenditure.contain,updated_data['contain'])
    
    def test_delete_expenditure(self):
        response = self.client.delete(f'/v1/api/expenditure/{self.expenditure.id}/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(Expenditure.objects.count(),0)