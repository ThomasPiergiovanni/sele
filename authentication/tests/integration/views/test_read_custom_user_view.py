# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)


class UpdateCustomUserViewTest(TestCase):

    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()

    def test_get_with_nominal_scenario(self):
        self.auth_emulation.emulate_custom_user()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/authentication/read_custom_user/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'authentication/read_custom_user.html'
        )

    def test_get_with_alternative_scenario(self):
        response = self.client.get(
            '/authentication/update_custom_user/', follow=True
        )
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
