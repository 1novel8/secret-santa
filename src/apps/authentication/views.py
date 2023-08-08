from rest_framework import status, mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .models import User
from .serializers import CreateUserSerializer, UpdateUserSerializer, RetrieveUserSerializer
from apps.core.mixins import SerializeByActionMixin, PermissionsByAction


class UserViewSet(SerializeByActionMixin,
                  PermissionsByAction,
                  GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin):
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
    permission_classes = (permissions.IsAuthenticated, )
    http_method_names = ['get', 'patch', 'post', 'delete']

    def perform_destroy(self, instance):
        if self.request.user.is_authenticated and instance == self.request.user:
            instance.delete()
            return
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            kwargs['partial'] = True
            return self.update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
