from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import Present
from .serializers import BasePresentSerializer


class PresentViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin):

    queryset = Present.objects.all()
    serializer_class = BasePresentSerializer
