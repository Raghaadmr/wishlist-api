from rest_framework.permissions import BasePermission

class OnlyAddedByUser(BasePermission):
    message = "you are not allowed"

    def has_object_permission(self, request, view, obj):
        if obj.added_by == request.user or request.user.is_staff:
            return True
        else:
            return False
