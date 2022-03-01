# pylint: disable=C0116, E1101
"""Test create custom user view module.
"""
from django.test import RequestFactory, TestCase
from django.urls import reverse

from authentication.forms.login_form import LoginForm
from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)


class LoginViewTest(TestCase):
    """Test CreateCustomUserView view class.
    """
    @classmethod
    def setUpTestData(cls):
        AuthenticationEmulation().emulate_custom_user()

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

    # def test_post_with_status_code_200(self):
    #     response = self.client.post(
    #         '/authentication/login/',
    #         data=self.form_data,
    #         follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    
    def test_post_with_valid_response_redirect(self):
        response = self.client.post(
            '/authentication/login/',
            data={
                'email': 'user1@email.com',
                'password': 'xxx_Xxxx'
            },
            follow=True
        )
        print(response.redirect_chain)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(
        #     response.redirect_chain[0][0],
        #     reverse('information:home')
        # )

    # def test_post_with_invalid_form_missing_input(self):
    #     response = self.client.post(
    #         '/authentication/create_custom_user/',
    #         data=self.form_data_no_pc,
    #         follow=True
    #     )
    #     self.assertEqual(response.templates[0].name, 'authentication/create_custom_user.html')
    #     self.assertIsInstance(response.context['form'], CreateCustomUserForm)
    #     self.assertTrue(response.context['form'].errors)

    # def test_post_with_invalid_form_wrong_input(self):
    #     response = self.client.post(
    #         '/authentication/create_custom_user/',
    #         data=self.form_data_pc_no_match,
    #         follow=True
    #     )
    #     self.assertEqual(response.templates[0].name, 'authentication/create_custom_user.html')
    #     self.assertIsInstance(response.context['form'], CreateCustomUserForm)
    #     self.assertFalse(response.context['form'].errors)
    #     self.assertEqual(
    #         response.context['messages']._loaded_data[0].level_tag, 'error'
    #     )
    #     self.assertEqual(
    #         response.context['messages']._loaded_data[0].message, 
    #         "Le couple \"code postal\" et \"ville\" n'est pas valide."
    #     )

    # def test_post_with_voting_saved(self):
    #     collectivity = Collectivity.objects.get(name__exact='Bagneux')
    #     self.assertEqual(collectivity.activity, 'no')
    #     self.client.post(
    #         '/authentication/create_custom_user/',
    #         data=self.form_data,
    #         follow=True
    #     )
    #     self.assertEqual(
    #         CustomUser.objects.all().last().user_name, 'UserNameT'
    #     )
    #     collectivity = Collectivity.objects.get(name__exact='Bagneux')
    #     self.assertEqual(collectivity.activity, 'yes')
