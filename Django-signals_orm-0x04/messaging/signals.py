from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from messaging.models import Message, Notification, MessageHistory

@receiver(post_delete, sender=User)
def cleanup_related_data(sender, instance, **kwargs):
    # Extra safety cleanup (not required if on_delete=CASCADE is used correctly)
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    Notification.objects.filter(user=instance).delete()
    # MessageHistory will be deleted automatically due to FK cascade from Message
