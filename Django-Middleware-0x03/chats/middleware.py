# Django-Middleware-0x03/chats/middleware.py

import logging
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Set up the logger
        self.logger = logging.getLogger('request_logger')
        handler = logging.FileHandler('requests.log')
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        path = request.path
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} - User: {user} - Path: {path}"
        self.logger.info(log_message)
        response = self.get_response(request)
        return response
from rest_framework import viewsets
from .models import Conversation, Message

from django.http import HttpResponse
from datetime import datetime, timedelta
from collections import defaultdict
import threading

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_log = defaultdict(list)  # {ip: [timestamps]}
        self.lock = threading.Lock()
        self.time_window = timedelta(minutes=1)
        self.message_limit = 5

    def __call__(self, request):
        if request.method == 'POST' and request.path.startswith('/api/messages/'):
            ip = self.get_client_ip(request)
            now = datetime.now()

            with self.lock:
                # Remove timestamps older than 1 minute
                self.message_log[ip] = [
                    timestamp for timestamp in self.message_log[ip]
                    if now - timestamp < self.time_window
                ]

                # Check if limit is exceeded
                if len(self.message_log[ip]) >= self.message_limit:
                    return HttpResponse(
                        "Rate limit exceeded: You can only send 5 messages per minute.",
                        status=429
                    )

                # Log current timestamp
                self.message_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
from rest_framework import permissions