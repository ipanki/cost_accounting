from rest_framework import serializers

from transactions.models import Category, Transaction


class ShowCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'user')


class EditCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class CreateAccountingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('organization', 'amount', 'category', 'income')


class ShowAccountingSerializer(serializers.ModelSerializer):
    tag = EditCategoriesSerializer()

    class Meta:
        model = Transaction
        fields = ('id', 'organization', 'amount',
                  'category', 'income', 'created_at')


class ReportRowSerializer(serializers.Serializer):
    categoryId = serializers.IntegerField(source='category__id')
    categoryName = serializers.CharField(source='category__name')
    total = serializers.IntegerField(source='amount')


class ReportSerializer(serializers.Serializer):
    expenses = ReportRowSerializer(many=True)
    incomes = ReportRowSerializer(many=True)
