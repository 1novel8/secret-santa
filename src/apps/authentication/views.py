import base64

from drf_spectacular.utils import extend_schema
from rest_framework import status, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .models import User
from .serializers import CreateUserSerializer, UpdateUserSerializer, RetrieveUserSerializer
from apps.core.mixins import SerializeByActionMixin, PermissionsByAction
from apps.core import mixins as custom_mixins
from .services import UserService


@extend_schema(tags=['user'])
class UserViewSet(SerializeByActionMixin,
                  PermissionsByAction,
                  GenericViewSet,
                  custom_mixins.CreateModelMixin,
                  custom_mixins.RetrieveModelMixin,
                  custom_mixins.DestroyModelMixin,
                  custom_mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serialize_by_action = {
        'retrieve': RetrieveUserSerializer,
        'create': CreateUserSerializer,
        'partial_update': UpdateUserSerializer,
        'destroy': RetrieveUserSerializer,
    }
    permissions_by_action = {
        'retrieve': [permissions.IsAuthenticated],
        'create': [permissions.AllowAny],
        'partial_update': [permissions.IsAuthenticated],
        'destroy': [permissions.IsAuthenticated],
    }
    permission_classes = (permissions.AllowAny, )

    service = UserService()

    http_method_names = ['get', 'patch', 'post', 'delete']

    def perform_create(self, **kwargs):
        if 'token' in self.request.query_params:
            kwargs['is_verified'] = True
            kwargs['email'] = decode_token(self.request.query_params.get('token'))
        else:
            kwargs['is_verified'] = False
        return self.service.create(**kwargs, password=self.request.data['password'])

    def perform_update(self, **kwargs):
        return self.service.update(user=self.request.user, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.service.delete(user=kwargs.get('user'), **kwargs)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        obj = self.service.get_by_id(**kwargs)
        serializer = self.get_serializer(instance=obj)

        return Response(serializer.data)


def decode_token(token_base64):
    token_bytes = base64.b64decode(token_base64.encode('utf-8'))
    data_parts = token_bytes.decode('utf-8').split(':')
    return data_parts[0]
