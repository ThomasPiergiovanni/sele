# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)


class LogoutViewTest(TestCase):

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
            response.redirect_chain[0][0], reverse('information:home')
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), None)

    def test_get_with_unauthenticated_user(self):
        response = self.client.get('/authentication/logout/', follow=True)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), None)
