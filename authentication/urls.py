"""Urls module
"""
from django.urls import path

from authentication.views.login_view import LoginView
from authentication.views.create_custom_user_view import CreateCustomUser


app_name = 'authentication'

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path(
        'create_custom_user/',
        CreateCustomUser.as_view(),
        name='create_custom_user'
    )
]
