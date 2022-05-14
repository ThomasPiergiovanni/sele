"""Test collectivity votings view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.forms.collectivity_discussions_form import CollectivityDiscussionsForm
from chat.models.discussion import Discussion
from chat.tests.emulation.chat_emulation import ChatEmulation


class CollectivityDIscussionsViewTest(TestCase):
    """Test CollectivityDiscussions view class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_discussion()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/chat/collectivity_discussions/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/discussions.html')
        self.assertIsInstance(
            response.context['form'], CollectivityDiscussionsForm
        )
        self.assertIsInstance(response.context['page_objects'][0], Discussion)
        self.assertEqual(response.context['page_objects'][0].id, 3)
        self.assertEqual(response.context['page_objects'][1].id, 2)
    
    def test_get_with_alternative_scenario_one(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        session = self.client.session
        session['c_d_v_f_search_input'] = 'JS'
        session.save()
        response = self.client.get(
            '/chat/collectivity_discussions/', follow=True
        )
        self.assertEqual(response.context['page_objects'][0].id,3)

    def test_get_with_alternative_scenario_two(self):
        response = self.client.get(
            '/chat/collectivity_discussions/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )

    def test_post_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form = {'search_input': 'JS', 'cdf_search_button': 'yes'}
        response = self.client.post(
            '/chat/collectivity_discussions/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/discussions.html')
        self.assertIsInstance(response.context['page_objects'][0], Discussion)
        self.assertEqual(response.context['page_objects'][0].id, 3)

    def test_post_with_alternative_scenario_one_missing_input(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form = {'search_input': '', 'cdf_search_button': 'yes'}
        response = self.client.post(
            '/chat/collectivity_discussions/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/discussions.html')
        self.assertIsInstance(response.context['page_objects'][0], Discussion)
        self.assertEqual(response.context['page_objects'][0].id, 3)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_alternative_scenario_two_missing_input(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form = {'search_input': '', 'cdf_clear_button': 'yes'}
        response = self.client.post(
            '/chat/collectivity_discussions/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/discussions.html')
        self.assertIsInstance(response.context['page_objects'][0], Discussion)
        self.assertEqual(response.context['page_objects'][0].id, 3)
        self.assertFalse(response.context['form'].errors)

    def test_post_with_alternative_scenario_three(self):
        form = {'search_input': 'JS', 'cdf_search_button': 'yes'}
        response = self.client.post(
            '/chat/collectivity_discussions/', data=form, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )
