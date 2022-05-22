# pylint: disable=C0114,C0115,C0116,E1101,W0212,R0801
from django.test import TestCase
from django.urls import reverse

from vote.models import Voting
from vote.tests.emulation.vote_emulation import VoteEmulation


class CollectivityVotingsViewTest(TestCase):

    def setUp(self):
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_test_setup()

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
        self.assertEqual(response.context['page_objects'][0].id, 1)

    def test_get_with_alternative_scenario_two(self):
        response = self.client.get('/vote/collectivity_votings/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
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
            response.redirect_chain[0][0], reverse('authentication:login')
        )
