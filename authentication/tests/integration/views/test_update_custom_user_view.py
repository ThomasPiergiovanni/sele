# pylint: disable=C0114,C0115,C0116,E1101,R0801,W0212
from django.test import TestCase
from django.urls import reverse

from authentication.forms.update_custom_user_form import (
    UpdateCustomUserForm
)
from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)


class UpdateCustomUserViewTest(TestCase):

    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.form_data = {
            'user_name': 'UserName1New',
            'collectivity': 'Bagneux',
            'postal_code': '92220',
        }
        self.form_data_no_pc = {
            'user_name': 'UserName',
            'collectivity': 'Bourg-la-Reine',
            'postal_code': '',
        }
        self.form_data_pc_no_match = {
            'user_name': 'UserName',
            'collectivity': 'Bourg-la-Reine',
            'postal_code': '92220',
        }

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/authentication/update_custom_user', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'authentication/update_custom_user.html'
        )
        self.assertIsInstance(response.context['form'], UpdateCustomUserForm)

    def test_get_with_alternative_scenario(self):
        response = self.client.get(
            '/authentication/update_custom_user/', follow=True
        )
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )

    def test_post_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/authentication/update_custom_user/',
            data=self.form_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('information:home')
        )
        self.assertEqual(
            CustomUser.objects.get(email__exact='user1@email.com').user_name,
            'UserName1New'
        )

    def test_post_with_alternative_scenario_form_missing_input(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/authentication/update_custom_user/',
            data=self.form_data_no_pc,
            follow=True
        )
        self.assertEqual(
            response.templates[0].name,
            'authentication/update_custom_user.html'
        )
        self.assertIsInstance(response.context['form'], UpdateCustomUserForm)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_alternative_scenario_form_wrong_input(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/authentication/update_custom_user/',
            data=self.form_data_pc_no_match,
            follow=True
        )
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.templates[0].name,
            'authentication/update_custom_user.html'
        )
        self.assertIsInstance(response.context['form'], UpdateCustomUserForm)
        self.assertFalse(response.context['form'].errors)
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(response_msg.message, "Code postal != Ville")
