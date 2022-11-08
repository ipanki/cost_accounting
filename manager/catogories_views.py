from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from manager.serializers import ShowCategoriesSerializer, EditCategoriesSerializer
from manager.models import Tag


class CategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ShowCategoriesSerializer
    queryset = Tag.objects

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return EditCategoriesSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
