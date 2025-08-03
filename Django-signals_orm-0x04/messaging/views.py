from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

@login_required
def delete_user(request):
    user = request.user
    logout(request)  # Log the user out before deleting
    user.delete()    # Trigger the deletion (and signals)
    return redirect('home')  # Redirect to homepage or login page
from .models import Message, Notification, MessageHistory
from django.db.models.signals import post_save