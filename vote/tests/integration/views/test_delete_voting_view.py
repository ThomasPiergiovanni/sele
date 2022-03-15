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
            response_msg.message, "Le crétaeur seulement peut "
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


    # def test_post_with_nominal_scenario(self):
    #     self.client.login(email='user1@email.com', password='xxx_Xxxx')
    #     response = self.client.post(
    #         '/vote/create_voting/', data=self.form_data, follow=True
    #     )
    #     response_msg = response.context['messages']._loaded_data[0]
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(
    #         Voting.objects.all().last().question, 'Ma question est'
    #     )
    #     self.assertEqual(
    #         response.redirect_chain[0][0], reverse('vote:overview')
    #     )
    #     self.assertEqual(response_msg.level_tag, 'success')
    #     self.assertEqual(response_msg.message, "Création réussie")
    
    # def test_post_with_alternative_scenario_with_wrong_form(self):
    #     self.client.login(email='user1@email.com', password='xxx_Xxxx')
    #     response = self.client.post(
    #         '/vote/create_voting/', data=self.wrong_form_data, follow=True
    #     )
    #     self.assertTemplateUsed(response, 'vote/create_voting.html')
    #     self.assertIsInstance(response.context['form'], VotingForm)
    #     self.assertTrue(response.context['form'].errors)

    # def test_post_with_alternative_scenario_with_unauthenticated_user(self):
    #     response = self.client.post(
    #         '/vote/create_voting/', data=self.form_data, follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     response_msg = response.context['messages']._loaded_data[0]
    #     self.assertEqual(
    #         response.redirect_chain[0][0],reverse('information:home')
    #     )
    #     self.assertEqual(response_msg.level_tag, 'error')
    #     self.assertEqual(response_msg.message, "Authentification requise")
