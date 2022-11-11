from django.contrib.auth.models import User
from django.test import TestCase

from transactions.models import Transaction
from transactions.services import get_balance


class BalanceTestCase(TestCase):
    def test_get_balance(self):
        self.user = User.objects.create(username='testuser', password='12345')
        category_income = self.user.categories.get(name='Зарплата')
        category_expense = self.user.categories.get(name='Машина')
        Transaction.objects.create(user=self.user, organization="TestOrg", amount=100,
                                   category=category_income, income=True)
        Transaction.objects.create(user=self.user, organization="TestOrg2", amount=15,
                                   category=category_expense, income=False)

        self.assertEqual(85, get_balance(self.user))
