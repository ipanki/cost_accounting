from django.db.models import Sum
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import filters

from manager.serializers import CreateAccountingSerializer, ShowAccountingSerializer, ReportSerializer
from manager.models import Transaction


class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = ShowAccountingSerializer
    queryset = Transaction.objects
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ['amount', 'created_at']

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CreateAccountingSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='balance')
    def show_balance(self, request):
        sum_expenses = Transaction.objects.filter(user=request.user, income=False).aggregate(expenses=Sum('amount'))
        sum_incomes = Transaction.objects.filter(user=request.user, income=True).aggregate(incomes=Sum('amount'))
        print(sum_expenses)
        return Response(status=status.HTTP_200_OK,
                        data=f"Your balance is {sum_incomes['incomes'] - sum_expenses['expenses']}$")

    @action(detail=False, methods=['get'])
    def report(self, request):
        stats = Transaction.objects.filter(user=request.user).values('tag__id', 'tag__name', 'income').annotate(
            amount=Sum('amount'))
        print(stats)
        return Response(status=status.HTTP_200_OK, data=ReportSerializer(
        {
            "incomes": filter(lambda row: row['income'], stats),
            "expenses": filter(lambda row: not row['income'], stats)
        }).data)





