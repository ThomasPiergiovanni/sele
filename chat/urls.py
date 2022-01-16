"""Urls module
"""
from django.urls import path

from chat.views.chat_view import ChatView



app_name = 'chat'

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat')
]
