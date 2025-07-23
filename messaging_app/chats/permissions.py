from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to authenticated users who are participants
    in the related conversation for message and conversation objects.
    """

    def has_permission(self, request, view):
        # Ensure user is authenticated for any request
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # For Conversation objects:
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()

        # For Message objects:
        if hasattr(obj, 'conversation'):
            return request.user in obj.conversation.participants.all()

        # Default deny
        return False
from rest_framework import viewsets
from .models import Conversation, Message
