"""Test collectivity votings view module.
"""
from django.test import TestCase
from django.urls import reverse

from vote.models.voting import Voting

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from vote.tests.emulation.vote_emulation import VoteEmulation


class CollectivityVotingsViewTest(TestCase):
    """Test CollectivityVotings view class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_voting_method()
        self.vote_emulation.emulate_voting()
        self.vote_emulation.emulate_vote()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/collectivity_votings/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/votings.html')
        self.assertIsInstance(response.context['page_objects'][0], Voting)
        self.assertEqual(response.context['page_objects'][0].id, 1)
        self.assertEqual(response.context['page_objects'][1].id, 3)
    
    def test_get_with_alternative_scenario_one(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        session = self.client.session
        session['c_v_v_f_search_input'] = 'nettoyage'
        session.save()
        response = self.client.get('/vote/collectivity_votings/', follow=True)
        self.assertEqual(response.context['page_objects'][0].id,1)

    def test_get_with_alternative_scenario_two(self):
        response = self.client.get('/vote/collectivity_votings/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )

    def test_post_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form = {'search_input': 'nettoyage', 'cvf_search_button': 'yes'}
        response = self.client.post(
            '/vote/collectivity_votings/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/votings.html')
        self.assertIsInstance(response.context['page_objects'][0], Voting)
        self.assertEqual(response.context['page_objects'][0].id, 1)

    def test_post_with_alternative_scenario_one_missing_input(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form = {'search_input': '', 'cvf_search_button': 'yes'}
        response = self.client.post(
            '/vote/collectivity_votings/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/votings.html')
        self.assertIsInstance(response.context['page_objects'][0], Voting)
        self.assertEqual(response.context['page_objects'][0].id, 1)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_alternative_scenario_two_missing_input(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form = {'search_input': '', 'cvf_clear_button': 'yes'}
        response = self.client.post(
            '/vote/collectivity_votings/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/votings.html')
        self.assertIsInstance(response.context['page_objects'][0], Voting)
        self.assertEqual(response.context['page_objects'][0].id, 1)
        self.assertFalse(response.context['form'].errors)

    def test_post_with_alternative_scenario_three(self):
        form = {'search_input': 'nettoyage', 'cvf_search_button': 'yes'}
        response = self.client.post(
            '/vote/collectivity_votings/', data=form, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )
