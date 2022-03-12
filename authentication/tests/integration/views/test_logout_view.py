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
        self.assertEqual(
            response.context['messages']._loaded_data[0].message, 
            "Déconnexion réussie"
        )
        self.assertEqual(
            response.context['messages']._loaded_data[0].level_tag, 
            "success"
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), None)

    def test_get_with_authenticated_user(self):
        self.authentication_emulation.emulate_custom_user()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        self.assertEqual(self.client.session.get('_auth_user_id'), '1')
        response = self.client.get('/authentication/logout/', follow=True)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), None)

    def test_get_with_unauthenticated_user(self):
        response = self.client.get('/authentication/logout/', follow=True)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0], reverse('information:home')
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), None)
        self.assertEqual(
            response_msg.message, "L'utilisateur est déja déconnecté"
        )
        self.assertEqual(response_msg.level_tag, "warning")