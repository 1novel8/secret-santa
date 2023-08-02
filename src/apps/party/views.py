from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions, status

from .models import Party
from .serializers import BasePartySerializer
from .services import PartyService
from apps.core import mixins as custom_mixins


class PartyViewSet(mixins.ListModelMixin,
                   custom_mixins.UpdateModelMixin,  # not realized
                   custom_mixins.RetrieveModelMixin,  # not realized
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

