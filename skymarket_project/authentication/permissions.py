from rest_framework import permissions

from users.models import User


class AdminGetPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role != User.ADMIN:
            return False
        return True


class GetUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == User.USER:
            return True
        elif request.user.role == User.ADMIN:
            return True
        else:
            return False
