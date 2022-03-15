"""Test delete voting view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from vote.forms.voting_form import VotingForm
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.emulation.vote_emulation import VoteEmulation


class DeleteVotingViewTest(TestCase):
    """Test DeleteVotingView class.
    """
    def setUp(self):
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_vote()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/detailed_voting.html')
        self.assertIsInstance(response.context['voting'], Voting)
        self.assertEqual(response.context['voting_status'], 'Fermé')
        self.assertEqual(response.context['voting_operation'], 'delete')
        self.assertEqual(response.context['voting_result'], 50)

    def test_get_with_first_alternative_scenario(self):
        self.client.login(email='user2@email.com', password='yyy_Yyyy')
        response = self.client.get('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0], reverse('vote:overview')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(
            response_msg.message, "Le créateur seulement peut "
            "supprimer la votation"
        )

    def test_get_with_second_alternative_scenario(self):
        response = self.client.get('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(response_msg.message, "Authentification requise")


    def test_post_with_authenticated_user(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('vote:overview')
        )
        try:
            voting = Voting.objects.get(pk=1)
        except:
            voting = False
        self.assertFalse(voting)
        self.assertEqual(
            response.context['messages']._loaded_data[0].message, 
            "Suppression de votation réussie"
        )
        self.assertEqual(
            response.context['messages']._loaded_data[0].level_tag, 
            "success"
        )

    def test_post_with_first_alternative_scenario(self):
        self.client.login(email='user2@email.com', password='yyy_Yyyy')
        response = self.client.post('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0], reverse('vote:overview')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(
            response_msg.message, "Le créateur seulement peut "
            "supprimer la votation"
        )

    def test_post_with_second_alternative_scenario(self):
        response = self.client.post('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(response_msg.message, "Authentification requise")
