"""Test reset vote module.
"""
from django.db import models
from django.test import TestCase

from authentication.management.commands.reset_authentication import Command
from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import CustomUserTest


class ResetAuthenticationTest(TestCase):
    """Test reset vote method class.
    """
    def setUp(self):
        """Method that set up data for the entire class
        """
        self.command = Command()

    def test_drop_custom_user_with_instance_is_none(self):
        CustomUserTest().emulate_custom_user()
        custom_user = CustomUser.objects.all()
        self.assertTrue(custom_user)
        self.command._Command__drop_custom_user()
        custom_user = CustomUser.objects.all()
        self.assertFalse(custom_user)
