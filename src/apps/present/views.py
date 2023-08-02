from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Present
from .serializers import BasePresentSerializer
from .services import PresentService
from apps.core import mixins as custom_mixins


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

