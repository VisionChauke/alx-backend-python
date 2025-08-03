from django.urls import path
from .views import delete_user

urlpatterns = [
    path('delete-account/', delete_user, name='delete_account'),
]
# This URL pattern maps the 'delete-account/' path to the delete_user view,
# which handles user deletion and cleanup of related data through signals.