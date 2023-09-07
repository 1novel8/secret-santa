from drf_spectacular.utils import extend_schema
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from apps.authentication.models import User
from apps.authentication.serializers import CreateUserSerializer, UpdateUserSerializer, RetrieveUserSerializer
from apps.authentication.services import UserService

from apps.core.mixins import SerializeByActionMixin, PermissionsByAction
from apps.core import mixins as custom_mixins
from apps.core.utils import decode_token


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
        'me': RetrieveUserSerializer,
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
        print(kwargs)
        if 'token' in kwargs:
            kwargs['is_verified'] = True
            kwargs['email'] = decode_token(kwargs.pop('token'))
        else:
            kwargs['is_verified'] = False
        return self.service.create(**kwargs)

    def perform_update(self, **kwargs):
        return self.service.update(user=self.request.user, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.service.delete(user=kwargs.get('user'), **kwargs)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        obj = self.service.get_by_id(**kwargs)
        serializer = self.get_serializer(instance=obj)

        return Response(serializer.data)

    @action(methods=["GET"], detail=False, url_path='me')
    def me(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.request.user)
        return Response(serializer.data)
