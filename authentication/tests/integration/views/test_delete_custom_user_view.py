# pylint: disable=C0116, E1101
"""Test delete custom user view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)


class DeleteCustomViewTest(TestCase):
    """Test DeleteCustomUserView class.
    """
    def setUp(self):
        self.authentication_emulation = AuthenticationEmulation()

    def test_get_with_view_template(self):
        self.authentication_emulation.emulate_custom_user()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/authentication/delete_custom_user/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('authentication/delete_custom_user.html')
        for message in response.context['messages']:  
            self.assertEqual(message.message, "Authentification requise")
            self.assertEqual(message.level_tag, "error")
        # self.assertEqual(self
        #     response.context['messages']._loaded_data[0].message, 
        #     "Compte utilisateur supprimé"
        # )
        # self.assertEqual(
        #     response.context['messages']._loaded_data[0].level_tag, 
        #     "success"
        # )


    def test_get_with_unauthentified_user(self):
        response = self.client.get(
            '/authentication/delete_custom_user/', follow=True
        )
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(self.client.session.get('_auth_user_id'), None)
        self.assertEqual(
            response.context['messages']._loaded_data[0].message, 
            "Authentification requise"
        )
        self.assertEqual(
            response.context['messages']._loaded_data[0].level_tag, 
            "error"
        )