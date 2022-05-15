"""Chat application and its configuration module.
"""
from django.apps import AppConfig


class ChatConfig(AppConfig):
    """Chat application and its configuration class.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
