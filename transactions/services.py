from django.db.models import Sum

from transactions.models import Transaction


def get_summary_report(user):
    stats = Transaction.objects.filter(user=user).values('category__id', 'category__name', 'income') \
        .annotate(amount=Sum('amount'))
    incomes = list(filter(lambda row: row['income'], stats))
    expenses = list(filter(lambda row: not row['income'], stats))
    return incomes, expenses


def get_balance(user):
    totals = Transaction.objects.filter(user=user).values(
        'income').annotate(total=Sum('amount'))
    balance = 0
    for row in totals:
        balance += row['total'] if row['income'] else -row['total']
    return balance
