from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.present.models import Present
from apps.present.serializers import BasePresentSerializer
from apps.present.services import PresentService
from apps.core import mixins as custom_mixins


@extend_schema(tags=['present'])
class PresentViewSet(mixins.ListModelMixin,
                     custom_mixins.UpdateModelMixin,
                     custom_mixins.RetrieveModelMixin,
                     custom_mixins.CreateModelMixin,
                     custom_mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Present.objects.all()
    serializer_class = BasePresentSerializer
    service = PresentService()

    http_method_names = ['get', 'patch', 'put', 'post', 'delete']

    def perform_create(self, **kwargs):
        return self.service.create(user=self.request.user, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.service.list(user=self.request.user, **kwargs)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
