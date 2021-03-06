# pylint: disable=C0114,C0115,C0116,E1101,R0201,W0212
from django.db import models
from django.test import TestCase

from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from collectivity.models import Collectivity


class CustomUserTest(TestCase):

    def setUp(self):
        AuthenticationEmulation().emulate_custom_user()

    def test_custom_user_with_custom_user_class(self):
        custom_user = CustomUser.objects.get(pk=1)
        self.assertIsInstance(custom_user, CustomUser)

    def test_custom_user_with_attr_email_characteristic(self):
        attribute = CustomUser._meta.get_field('email')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.EmailField()))
        self.assertEqual(attribute.max_length, 128)
        self.assertEqual(attribute.unique, True)

    def test_custom_user_with_attr_user_name_characteristic(self):
        attribute = CustomUser._meta.get_field('user_name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.TextField()))
        self.assertEqual(attribute.max_length, 64)

    def test_custom_user_with_attr_balance_characteristic(self):
        attribute = CustomUser._meta.get_field('balance')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.BigIntegerField()))

    def test_custom_user_with_attr_collectivity_characteristic(self):
        attribute = CustomUser._meta.get_field('collectivity')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Collectivity, on_delete=models.CASCADE))
        )

    def test_custom_user_with_emulated_custom_user_instance(self):
        custom_user = CustomUser.objects.get(pk=1)
        self.assertEqual(custom_user.email, "user1@email.com")
        custom_user = CustomUser.objects.get(pk=2)
        self.assertEqual(custom_user.email, "user2@email.com")
