
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