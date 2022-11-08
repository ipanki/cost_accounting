from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from transactions.serializers import ShowCategoriesSerializer, EditCategoriesSerializer
from transactions.models import Category


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
