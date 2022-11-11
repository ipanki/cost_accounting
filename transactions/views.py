from django.db.models import Sum
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from transactions.models import Category, Transaction
from transactions.serializers import (CreateAccountingSerializer,
                                      EditCategoriesSerializer,
                                      ReportSerializer,
                                      ShowAccountingSerializer,
                                      ShowCategoriesSerializer)
from transactions.services import get_balance, get_summary_report


class CategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShowCategoriesSerializer
    queryset = Category.objects

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return EditCategoriesSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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


class ReportsViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'], url_path='balance')
    def show_balance(self, request):
        return Response(status=status.HTTP_200_OK, data=get_balance(request.user))

    @action(detail=False, methods=['get'])
    def summary(self, request):
        incomes, expenses = get_summary_report(request.user)
        return Response(status=status.HTTP_200_OK, data=ReportSerializer(
            {
                "incomes": incomes,
                "expenses": expenses
            }).data)
