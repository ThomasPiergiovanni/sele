# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase
from django.urls import reverse

from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)


class DeleteCustomViewTest(TestCase):

    def setUp(self):
        self.authentication_emulation = AuthenticationEmulation()

    def test_get_with_authenticated(self):
        self.authentication_emulation.emulate_custom_user()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/authentication/delete_custom_user/', follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_get_with_unauthenticated_user(self):
        response = self.client.get(
            '/authentication/delete_custom_user/', follow=True
        )
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), None)

    def test_post_with_authenticated_user(self):
        self.authentication_emulation.emulate_custom_user()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/authentication/delete_custom_user/',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('information:home')
        )
        try:
            custom_user = CustomUser.objects.get(
                email__exact='user1@email.com'
            )
        except CustomUser.DoesNotExist:
            custom_user = False
        self.assertFalse(custom_user)
        self.assertEqual(
            response.context['messages']._loaded_data[0].message,
            "Suppression de compte réussie"
        )
        self.assertEqual(
            response.context['messages']._loaded_data[0].level_tag,
            "success"
        )

    def test_post_with_unauthenticated_user(self):
        self.authentication_emulation.emulate_custom_user()
        response = self.client.post(
            '/authentication/delete_custom_user/',
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
        try:
            custom_user = CustomUser.objects.get(
                email__exact='user1@email.com'
            )
        except CustomUser.DoesNotExist:
            custom_user = False
        self.assertTrue(custom_user)
