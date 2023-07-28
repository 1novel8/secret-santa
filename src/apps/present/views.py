from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status

from .models import Present
from .serializers import BasePresentSerializer
from .services import PresentService


class PresentViewSet(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Present.objects.all()
    serializer_class = BasePresentSerializer
    service = PresentService()

    http_method_names = ['get', 'patch', 'put', 'post', 'delete']

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        instance = self.service.create_present(**serializer.data)

        serializer = self.get_serializer(instance=instance)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()

        instance = self.service.update_present(**kwargs, **serializer.data)
        serializer = self.get_serializer(instance=instance)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.service.delete_present(**kwargs)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.service.get_present_by_id(**kwargs)
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
