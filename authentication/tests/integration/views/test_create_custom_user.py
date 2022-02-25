# pylint: disable=C0116, E1101
"""Test create custom user view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.forms.create_custom_user_form import CreateCustomUserForm
from authentication.models import CustomUser
from collectivity.tests.unit.models.test_collectivity import CollectivityTest


class CreateCustomUserTest(TestCase):
    """Test CreateCustomUser view class.
    """
    def setUp(self):
        CollectivityTest().emulate_collectivity()
        CollectivityTest().emulate_set_collectivity_postal_code()
        self.form_data = {
            'email': 'user@email.com',
            'password1': 'xxxx_Xxxx',
            'password2': 'xxxx_Xxxx',
            'user_name': 'UserNameT',
            'collectivity': 'Bourg-la-Reine',
            'postal_code': '92340',
        }
        self.wrong_form_data = {
            'email': 'user@email.com',
            'password1': 'xxxx_Xxxx',
            'password2': 'xxxx_Xxxx',
            'user_name': 'UserName',
            'collectivity': 'Bourg-la-Reine',
            'postal_code': '',
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
        self.assertEqual(response.redirect_chain[0][0], reverse('information:home'))

    def test_post_with_invalid_response(self):
        response = self.client.post(
            '/authentication/create_custom_user/',
            data=self.wrong_form_data,
            follow=True
        )
        # for message in response.context['messages']:
        #     self.assertEqual(message.level_tag, 'error')
        #     self.assertEqual(
        #         message.message, 
        #         "Une ou plusieurs informations a été incorrectement"
        #             "saisie Veuiller ressaisir le information!"
        #     )
        self.assertEqual(response.redirect_chain[0][0], reverse('authentication:create_custom_user'))

    def test_post_with_voting_saved(self):
        self.client.post(
            '/authentication/create_custom_user/',
            data=self.form_data,
            follow=True
        )
        new_custom_user = CustomUser.objects.all().order_by('-id')[0]
        self.assertEqual(new_custom_user.user_name, 'UserNameT')
