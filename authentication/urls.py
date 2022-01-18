"""Urls module
"""
from django.urls import path

from authentication.views.login_view import LoginView
from authentication.views.register_view import RegisterView


app_name = 'authentication'

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(), name='register')
]
