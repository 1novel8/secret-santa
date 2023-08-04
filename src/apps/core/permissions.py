from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Allows access only to owners users.
    """

    # def has_permission(self, request, view):
    #     return bool(request.user and request.user.is_authenticated)
