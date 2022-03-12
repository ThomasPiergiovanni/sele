# pylint: disable=C0116, E1101
"""Test read custom user view module.
"""
from django.contrib.auth import logout
from django.test import TestCase
from django.urls import reverse

from authentication.forms.edit_custom_user_form import EditCustomUserForm
from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import AuthenticationEmulation
from collectivity.models.collectivity import Collectivity
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)


class EditCustomUserViewTest(TestCase):
    """Test EditCustomUserView view class.
    """
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
            '/authentication/edit_custom_user/', follow=True
        )
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('information:home')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(response_msg.message, "Authentification requise")
