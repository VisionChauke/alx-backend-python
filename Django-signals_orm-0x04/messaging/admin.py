from django.contrib import admin
from .models import Message, Notification

admin.site.register(Message)
admin.site.register(Notification)
        print(f"Notification created for {instance.receiver} about message {instance.id}")
        # Optionally, you can log or print a message