from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import BankAccount
from .serializers import BankAccountSerializer

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
        bank_data_with_user_id = {
            'userId': self.user.id,
            'name': 'NH',
            'balance': 10000,
        }
        response = self.client.post('/v1/api/account/',data=bank_data_with_user_id,format='json')
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