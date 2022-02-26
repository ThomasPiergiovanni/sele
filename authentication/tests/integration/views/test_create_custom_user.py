# pylint: disable=C0116, E1101
"""Test create custom user view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.forms.create_custom_user_form import CreateCustomUserForm
from authentication.models import CustomUser
from collectivity.models.collectivity import Collectivity
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)


class CreateCustomUserViewTest(TestCase):
    """Test CreateCustomUserView view class.
    """
    def setUp(self):
        CollectivityEmulation().emulate_postal_code()
        CollectivityEmulation().emulate_collectivity()
        CollectivityEmulation().emulate_set_collectivity_postal_code()
        self.form_data = {
            'email': 'user@email.com',
            'password1': 'xxxx_Xxxx',
            'password2': 'xxxx_Xxxx',
            'user_name': 'UserNameT',
            'collectivity': 'Bagneux',
            'postal_code': '92220',
        }
        self.form_data_no_pc = {
            'email': 'user@email.com',
            'password1': 'xxxx_Xxxx',
            'password2': 'xxxx_Xxxx',
            'user_name': 'UserName',
            'collectivity': 'Bourg-la-Reine',
            'postal_code': '',
        }
        self.form_data_pc_no_match = {
            'email': 'user@email.com',
            'password1': 'xxxx_Xxxx',
            'password2': 'xxxx_Xxxx',
            'user_name': 'UserName',
            'collectivity': 'Bourg-la-Reine',
            'postal_code': '92220',
        }

    def test_get_with_status_code_200(self):
        response = self.client.get('/authentication/create_custom_user/')
        self.assertEqual(response.status_code, 200)

    def test_get_with_get_template(self):
        response = self.client.get('/authentication/create_custom_user/')
        self.assertTemplateUsed(
            response, 'authentication/create_custom_user.html'
        )

    def test_get_with_voting_form(self):
        response = self.client.get('/authentication/create_custom_user/')
        self.assertIsInstance(response.context['form'], CreateCustomUserForm)

    def test_post_with_status_code_200(self):
        response = self.client.post(
            '/authentication/create_custom_user/',
            data=self.form_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
    
    def test_post_with_valid_response_redirect(self):
        response = self.client.post(
            '/authentication/create_custom_user/',
            data=self.form_data,
            follow=True
        )
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('authentication:login')
        )

    def test_post_with_invalid_form_missing_input(self):
        response = self.client.post(
            '/authentication/create_custom_user/',
            data=self.form_data_no_pc,
            follow=True
        )
        self.assertEqual(response.templates[0].name, 'authentication/create_custom_user.html')
        self.assertIsInstance(response.context['form'], CreateCustomUserForm)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_invalid_form_wrong_input(self):
        response = self.client.post(
            '/authentication/create_custom_user/',
            data=self.form_data_pc_no_match,
            follow=True
        )
        self.assertEqual(response.templates[0].name, 'authentication/create_custom_user.html')
        self.assertIsInstance(response.context['form'], CreateCustomUserForm)
        self.assertFalse(response.context['form'].errors)
        self.assertEqual(
            response.context['messages']._loaded_data[0].level_tag, 'error'
        )
        self.assertEqual(
            response.context['messages']._loaded_data[0].message, 
            "Le couple \"code postal\" et \"ville\" n'est pas valide."
        )

    def test_post_with_voting_saved(self):
        collectivity = Collectivity.objects.get(name__exact='Bagneux')
        self.assertEqual(collectivity.activity, 'no')
        self.client.post(
            '/authentication/create_custom_user/',
            data=self.form_data,
            follow=True
        )
        self.assertEqual(
            CustomUser.objects.all().last().user_name, 'UserNameT'
        )
        collectivity = Collectivity.objects.get(name__exact='Bagneux')
        self.assertEqual(collectivity.activity, 'yes')
