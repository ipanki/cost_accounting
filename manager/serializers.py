from rest_framework import serializers
from django.contrib.auth.models import User
from manager.models import Tag, Transaction


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
        model = Tag
        fields = ('id', 'name', 'user')


class EditCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class CreateAccountingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('organization', 'amount', 'tag', 'income')


class ShowAccountingSerializer(serializers.ModelSerializer):
    tag = EditCategoriesSerializer()

    class Meta:
        model = Transaction
        fields = ('id', 'organization', 'amount', 'tag', 'income', 'created_at')


class ReportRowSerializer(serializers.Serializer):
    tagId = serializers.IntegerField(source='tag__id')
    tagName = serializers.CharField(source='tag__name')
    total = serializers.IntegerField(source='amount')


class ReportSerializer(serializers.Serializer):
    expenses = ReportRowSerializer(many=True)
    incomes = ReportRowSerializer(many=True)



