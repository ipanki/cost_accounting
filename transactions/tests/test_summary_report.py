from django.test import TestCase
from transactions.services import get_summary_report
from django.contrib.auth.models import User
from transactions.models import Transaction


class SummaryReportTestCase(TestCase):
    def test_get_summary_report(self):
        self.user = User.objects.create(username='testuser', password='12345')
        category_income = self.user.categories.get(name='Зарплата')
        category_expense = self.user.categories.get(name='Машина')
        Transaction.objects.create(user=self.user, organization="TestOrg", amount=100,
                                   category=category_income, income=True)
        Transaction.objects.create(user=self.user, organization="TestOrg2", amount=15,
                                   category=category_expense, income=False)

        incomes, expenses = get_summary_report(self.user)

        self.assertEqual(1, len(incomes))
        self.assertEqual(1, len(expenses))

        self.assertEqual({'category__id': category_income.id, 'category__name': 'Зарплата', 'income': True, 'amount': 100}, incomes[0])
        self.assertEqual({'category__id': category_expense.id, 'category__name': 'Машина', 'income': False, 'amount': 15}, expenses[0])