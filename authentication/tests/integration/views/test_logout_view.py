# pylint: disable=C0116, E1101
"""Test create custom user view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)


class LogoutViewTest(TestCase):
    """Test LogoutView class.
    """
    def setUp(self):
        self.authentication_emulation = AuthenticationEmulation()

    def test_get_with_nominal_view_name(self):
        self.authentication_emulation.emulate_custom_user()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/authentication/logout/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('information:home')
        )
        for message in response.context['messages']:
            self.assertEqual(message.message, "Déconnexion réussie")
            self.assertEqual(message.level_tag, "success")

    def test_get_with_authentified_user(self):
        self.authentication_emulation.emulate_custom_user()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        self.assertEqual(self.client.session.get('_auth_user_id'), '1')
        response = self.client.get('/authentication/logout/', follow=True)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), None)

    def test_get_with_unauthentified_user(self):
        response = self.client.get('/authentication/logout/', follow=True)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), None)