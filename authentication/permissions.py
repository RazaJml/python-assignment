"""
Permissions for authentication API.
"""
from rest_framework import permissions

from utils import is_admin


class IsSelfOrAdmin(permissions.BasePermission):
    """
    This permission is only applicable to UserViewSet and will allow users to make operations on themselves
    and will allow all operations on all users for admins.
    """
    def has_object_permission(self, request, view, obj):
        if is_admin(request.user):
            return True
        return obj == request.user
