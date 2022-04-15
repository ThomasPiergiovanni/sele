# pylint: disable=C0116, E1101
"""Test create discussion view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.forms.discussion_form import DiscussionForm
from chat.models.discussion import Discussion
from chat.tests.emulation.chat_emulation import ChatEmulation


class CreateDiscussionViewTest(TestCase):
    """Test CreateDIscussionView class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        # self.chat_emulation = ChatEmulation()
        # self.chat_emulation.emulate_discussion()
        self.form_data = {
            'subject': 'Le sujet est'
        }
        self.wrong_form_data = {
            'subject': ''
        }

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/chat/create_discussion/',follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/create_discussion.html')
        self.assertIsInstance(response.context['form'], DiscussionForm)

    def test_get_with_alternative_scenario(self):
        response = self.client.get('/chat/create_discussion/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )

    def test_post_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/chat/create_discussion/', data=self.form_data, follow=True
        )
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Discussion.objects.all().last().subject, 'Le sujet est'
        )
        self.assertEqual(
            Discussion.objects.all().last().discussion_discussion_type,
            None
        )
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('chat:collectivity_discussions')
        )
        self.assertEqual(response_msg.level_tag, 'success')
        self.assertEqual(response_msg.message, "Création réussie")
    
    def test_post_with_alternative_scenario_with_wrong_form(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/chat/create_discussion/', data=self.wrong_form_data, follow=True
        )
        self.assertTemplateUsed(response, 'chat/create_discussion.html')
        self.assertIsInstance(response.context['form'], DiscussionForm)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_alternative_scenario_with_unauthenticated_user(self):
        response = self.client.post(
            '/chat/create_discussion/', data=self.form_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )

