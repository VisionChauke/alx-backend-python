from rest_framework import permissions

class IsParticipant(permissions.BasePermission):
    """
    Custom permission to allow only conversation participants to access.
    """

    def has_object_permission(self, request, view, obj):
        # Assuming obj is a Conversation or Message with participants or sender
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        if hasattr(obj, 'sender'):
            return obj.sender == request.user
        return False
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    """

    def has_permission(self, request, view):
        # Allow read-only access for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write access only for admin users
        return request.user and request.user.is_staff