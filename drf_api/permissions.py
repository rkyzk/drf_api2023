"""
This module holds a permission class
that check if the current user is the owner
of the object, if permission is required.
"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        If poermission is required, check if
        the current user is the owner
        of the object.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
