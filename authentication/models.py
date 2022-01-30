"""CustomUser model module.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.management.engine.custom_user_manager import CustomUserManager
from collectivity.models.collectivity import Collectivity


class CustomUser(AbstractUser):
    """CustomUser model class. It sa an abstarct of django user class which
    provides all user authentication, login, etc. methods. Implemented in
    order to have email as identifier instead of username provided by default
    by django framework.
    """
    username = None
    email = models.EmailField(_('email address'), max_length=256, unique=True)
    user_name = models.TextField(_('username'), max_length=64, null=False)
    balance = models.BigIntegerField(default=0)
    collectivity = models.ForeignKey(Collectivity, models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
