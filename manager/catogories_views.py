from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from manager.serializers import ShowCategoriesSerializer, EditCategoriesSerializer
from manager.models import Tag


class CategoriesViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """Show all categories"""
        categories = Tag.objects.filter(user=request.user)
        serializer = ShowCategoriesSerializer(categories, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        form = EditCategoriesSerializer(data=request.data, instance=tag)
        form.is_valid(raise_exception=True)
        profile = form.save()
        return Response(status=status.HTTP_201_CREATED, data=EditCategoriesSerializer(profile).data)

    def create(self, request):
        """Create a new page"""
        tag = EditCategoriesSerializer(data=request.data)
        tag.is_valid(raise_exception=True)
        profile = tag.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED, data=EditCategoriesSerializer(profile).data)

    def delete(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        if request.user == tag.user:
            tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
