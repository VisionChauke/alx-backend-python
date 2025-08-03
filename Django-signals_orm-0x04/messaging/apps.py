from django.apps import AppConfig

class MessagingConfig(AppConfig):
    name = 'messaging'

    def ready(self):
        import messaging.signals
        # Ensure signals are imported when the app is ready
        # This will register the signal handlers defined in messaging/signals.py