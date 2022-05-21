# pylint: disable=C0103
"""Authentication urls module.
"""
from django.urls import path

from authentication.views.delete_custom_user_view import DeleteCustomUserView
from authentication.views.login_view import LoginView
from authentication.views.logout_view import LogoutView
from authentication.views.create_custom_user_view import CreateCustomUserView
from authentication.views.update_custom_user_view import UpdateCustomUserView
from authentication.views.read_custom_user_view import ReadCustomUserView

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'create_custom_user/',
        CreateCustomUserView.as_view(),
        name='create_custom_user'
    ),
    path(
        'delete_custom_user/',
        DeleteCustomUserView.as_view(),
        name='delete_custom_user'
    ),
    path(
        'update_custom_user/',
        UpdateCustomUserView.as_view(),
        name='update_custom_user'
    ),
    path(
        'read_custom_user/',
        ReadCustomUserView.as_view(),
        name='read_custom_user'
    ),
]
