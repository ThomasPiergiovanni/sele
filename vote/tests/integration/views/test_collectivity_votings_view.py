"""Test collectivity votings view module.
"""
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase
from django.urls import reverse

from vote.models.voting import Voting
from vote.tests.emulation.vote_emulation import VoteEmulation


class CollectivityVotingsViewTest(TestCase):
    """Test CollectivityVotings view class.
    """
    def setUp(self):
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_vote()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/collectivity_votings/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/votings.html')
        self.assertIsInstance(response.context['page_objects'][0], Voting)
        self.assertEqual(
            response.context['page_objects'][0].question,
            "Voulez-vous créer une demande de python?"
        )
        self.assertEqual(
            response.context['page_objects'][1].question,
            "Voulez-vous créer une demande de nettoyage?"
        )
    
    def test_get_with_alternative_scenario_one(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        session = self.client.session
        session['c_v_v_f_attribute'] = 'date'
        session['c_v_v_f_order'] = 'asc'
        session.save()
        response = self.client.get('/vote/collectivity_votings/', follow=True)
        self.assertEqual(
            response.context['page_objects'][0].question,
            "Voulez-vous créer une demande de nettoyage?"
        )

    def test_get_with_alternative_scenario_two(self):
        response = self.client.get('/vote/collectivity_votings/', follow=True)
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(response_msg.message, "Authentification requise")
