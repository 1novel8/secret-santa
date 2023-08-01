from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status

from .models import Present
from .serializers import BasePresentSerializer
from .services import PresentService
from src.apps.core import mixins as custom_mixins


class PresentViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     custom_mixins.UpdateModelMixin,
                     custom_mixins.RetrieveModelMixin,
                     custom_mixins.CreateModelMixin,
                     custom_mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Present.objects.all()
    serializer_class = BasePresentSerializer
    service = PresentService()

    http_method_names = ['get', 'patch', 'put', 'post', 'delete']

