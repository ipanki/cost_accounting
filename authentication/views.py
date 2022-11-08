from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.decorators import permission_classes

from transactions.serializers import RegistrationSerializer
from authentication.middleware import login_user
from authentication.services import adding_categories


class RegistrationViewSet(ViewSet):
    @permission_classes([AllowAny])
    @action(detail=False, methods=['post'])
    def signup(self, request):
        user = request.data.get('username')
        password = request.data.get('password')
        serializer = RegistrationSerializer(data={'username': user, 'password': password})
        serializer.is_valid(raise_exception=True)
        new_user = serializer.save()
        adding_categories(new_user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @permission_classes([AllowAny])
    @action(detail=False, methods=['post'])
    def login(self, request):
        data = login_user(request.data.get('username'), request.data.get('password'))

        return Response(data=data, status=status.HTTP_201_CREATED)