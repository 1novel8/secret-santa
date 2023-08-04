from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions, status

from .models import Party
from .serializers import BasePartySerializer
from .services import PartyService
from apps.core import mixins as custom_mixins


class PartyViewSet(mixins.ListModelMixin,
                   custom_mixins.UpdateModelMixin,  # done
                   custom_mixins.RetrieveModelMixin,  # done
                   custom_mixins.CreateModelMixin,  # done
                   custom_mixins.DestroyModelMixin,  # done
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
