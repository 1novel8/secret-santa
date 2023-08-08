from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions, status

from .models import Party
from .serializers import BasePartySerializer
from .services import PartyService
from apps.core import mixins as custom_mixins


@extend_schema(tags=['party'])
class PartyViewSet(mixins.ListModelMixin,
                   custom_mixins.UpdateModelMixin,
                   custom_mixins.RetrieveModelMixin,
                   custom_mixins.CreateModelMixin,
                   custom_mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Party.objects.all()
    serializer_class = BasePartySerializer
    service = PartyService()

    permission_classes = (permissions.IsAuthenticated, )

    http_method_names = ['get', 'patch', 'put', 'post', 'delete']

    def perform_create(self, **kwargs):
        return self.service.create(user=self.request.user, **kwargs)

    def perform_update(self, **kwargs):
        return self.service.update(user=self.request.user, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        obj = self.service.get_by_id(user=self.request.user, **kwargs)
        serializer = self.get_serializer(instance=obj)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.service.delete(user=kwargs.get('user'), **kwargs)

        return Response(status=status.HTTP_204_NO_CONTENT)
