from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from transactions.models import Transaction


class TransactionApiUserTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', password='12345')
        cls.category_income = cls.user.categories.get(name='Зарплата')
        cls.category_expense = cls.user.categories.get(name='Машина')
        Transaction.objects.create(user=cls.user, organization="TestOrg",
                                   amount=100, category=cls.category_income, income=True)
        Transaction.objects.create(user=cls.user, organization="TestOrg",
                                   amount=15, category=cls.category_expense, income=False)

    def setUp(self):
        self.client.login(username=self.user.username, password="12345")

    def test_get_summary_report(self):
        url = reverse('report-summary')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(1, len(response.data['incomes']))
        self.assertEqual(1, len(response.data['expenses']))

        self.assertEqual({'categoryId': self.category_income.id,
                          'categoryName': self.category_income.name,
                          'total': 100},
                         response.data['incomes'][0])
        self.assertEqual(100, response.data['incomes'][0]['total'])

        self.assertEqual({'categoryId': self.category_expense.id,
                          'categoryName': self.category_expense.name, 'total': 15},
                         response.data['expenses'][0])
        self.assertEqual(15, response.data['expenses'][0]['total'])
