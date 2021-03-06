# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase
from django.urls import reverse

from authentication.forms.login_form import LoginForm
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)


class LoginViewTest(TestCase):
    """Test CreateCustomUserView view class.
    """
    def setUp(self):
        self.authentication_emulation = AuthenticationEmulation()
        self.authentication_emulation.emulate_custom_user()
        self.form = {
                'username': 'user1@email.com',
                'password': 'xxx_Xxxx'
            }
        self.form_wrong_pwd = {
                'username': 'user1@email.com',
                'password': 'xxx_Yxxx'
            }
        self.form_empty_pwd = {
                'username': 'user1@email.com',
                'password': ''
            }

    def test_get_with_status_code_200(self):
        response = self.client.get('/authentication/login/')
        self.assertEqual(response.status_code, 200)

    def test_get_with_nominal_template(self):
        response = self.client.get('/authentication/login/')
        self.assertTemplateUsed(
            response, 'authentication/login.html'
        )

    def test_get_with_login_form(self):
        response = self.client.get('/authentication/login/')
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_post_with_valid_response_redirect(self):
        response = self.client.post(
            '/authentication/login/', data=self.form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('information:home')
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), "1")
        self.assertEqual(
            response.context['messages']._loaded_data[0].message,
            "Authentification réussie"
        )
        self.assertEqual(
            response.context['messages']._loaded_data[0].level_tag,
            "success"
        )

    def test_post_with_form_empty_pwd(self):
        response = self.client.post(
            '/authentication/login/', data=self.form_empty_pwd, follow=True
        )
        self.assertEqual(
            response.templates[0].name, 'authentication/login.html'
        )
        self.assertIsInstance(response.context['form'], LoginForm)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_form_wrong_pwd(self):
        response = self.client.post(
            '/authentication/login/', data=self.form_wrong_pwd, follow=True
        )
        self.assertEqual(
            response.templates[0].name, 'authentication/login.html'
        )
        self.assertIsInstance(response.context['form'], LoginForm)
        self.assertTrue(response.context['form'].errors)
