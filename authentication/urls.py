"""Urls module
"""
from django.urls import path

from authentication.views.login_view import LoginView
from authentication.views.create_custom_user_view import CreateCustomUserView
from authentication.views.edit_custom_user_view import EditCustomUserView

app_name = 'authentication'

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path(
        'create_custom_user/',
        CreateCustomUserView.as_view(),
        name='create_custom_user'
    ),
    path(
        'edit_custom_user/',
        EditCustomUserView.as_view(),
        name='edit_custom_user'
    ),
]
