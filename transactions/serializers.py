from django.contrib.auth.models import User
from rest_framework import serializers

from transactions.models import Category, Transaction


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


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
    tagId = serializers.IntegerField(source='category__id')
    tagName = serializers.CharField(source='category__name')
    total = serializers.IntegerField(source='amount')


class ReportSerializer(serializers.Serializer):
    expenses = ReportRowSerializer(many=True)
    incomes = ReportRowSerializer(many=True)
