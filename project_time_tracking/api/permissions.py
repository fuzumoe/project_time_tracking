from rest_framework import permissions

from project_time_tracking.api.models.user import User


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return int(view.kwargs['pk']) == request.user.id or request.user.is_superuser == True