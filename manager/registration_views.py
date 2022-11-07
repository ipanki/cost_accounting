from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.decorators import  permission_classes

from manager.serializers import RegistrationSerializer
from manager.utils import login_user
from manager.services import adding_categories


class RegistrationViewSet(ViewSet):
    @permission_classes([AllowAny])
    @action(detail=False, methods=['post'])
    def signup(self, request):
        user = request.data.get('username')
        password = request.data.get('password')
        serializer = RegistrationSerializer(data={'username': user, 'password': password})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        adding_categories(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @permission_classes([AllowAny])
    @action(detail=False, methods=['post'])
    def login(self, request):
        data = login_user(request.data.get('username'), request.data.get('password'))

        return Response(data=data, status=status.HTTP_201_CREATED)