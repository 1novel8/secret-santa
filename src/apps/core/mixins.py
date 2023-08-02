from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings


class SerializeByActionMixin:
    def get_serializer_class(self):
        try:
            return self.serialize_by_action[self.action]
        except Exception:
            return super().get_serializer_class()


class PermissionsByAction:
    def get_permissions(self):
        try:
            permission_classes = self.permissions_by_action[self.action]
        except Exception:
            permission_classes = super().get_permissions
        finally:
            return [permission() for permission in permission_classes]


class UpdateModelMixin:
    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        obj = self.perform_update(**kwargs, **serializer.data)
        serializer = self.get_serializer(instance=obj)

        if getattr(obj, '_prefetched_objects_cache', None):
            obj._prefetched_objects_cache = {}
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_update(self, **kwargs):
        return self.service.update(**kwargs)


class RetrieveModelMixin:
    """
    Retrieve model by id
    """
    def retrieve(self, request, *args, **kwargs):
        obj = self.service.get_by_id(**kwargs)
        serializer = self.get_serializer(instance=obj)

        return Response(serializer.data)


class CreateModelMixin:
    """
    Create a model instance.
    """
    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(**serializer.data)

        serializer = self.get_serializer(instance=obj)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, **kwargs):
        return self.service.create(**kwargs)


class DestroyModelMixin:
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        self.service.delete(**kwargs)

        return Response(status=status.HTTP_204_NO_CONTENT)