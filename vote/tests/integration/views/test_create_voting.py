# pylint: disable=C0116, E1101
"""Test add voting view module.
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


class CreateVotingTest(TestCase):
    """Test CreateVoting view class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.vote_emulation = VoteEmulation()
        self.form_data = {
            'question': 'Ma question est',
            'description': 'dsdss',
            'opening_date': "2022-01-02",
            'closure_date': "2022-01-25",
            'voting_method': VotingMethod.objects.get(pk=1).id
        }
        self.wrong_form_data = {
            'question': "",
            'description': 'dsdss',
            'opening_date': "2022-01-02",
            'closure_date': "2022-01-25",
            'voting_method': VotingMethod.objects.get(pk=1).id
        }
        # self.client.login(email='testuser@email.com', password='_Xxxxxxx')

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/create_voting/',follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/create_voting.html')
        self.assertIsInstance(response.context['voting_form'], VotingForm)

    def test_get_with_alternative_scenario(self):
        response = self.client.get('/vote/create_voting/', follow=True)
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(response_msg.message, "Authentification requise")


    def test_post_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/vote/create_voting/', data=self.form_data, follow=True
        )
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Voting.objects.all().last().question, 'Ma question est'
        )
        self.assertEqual(
            response.redirect_chain[0][0], reverse('vote:overview')
        )
        self.assertEqual(response_msg.level_tag, 'success')
        self.assertEqual(response_msg.message, "Votation créée")
    

    # def test_post_with_alternative_scenario_with_wrong_form(self):
    #     self.client.login(email='user1@email.com', password='xxx_Xxxx')
    #     response = self.client.post(
    #         '/vote/create_voting/', data=self.wrong_form_data, follow=True
    #     )
    #     response_msg = response.context['messages']._loaded_data[0]
    #     for message in response.context['messages']:
    #         self.assertEqual(message.level_tag, 'error')
    #         self.assertEqual(
    #             message.message, 
    #             "Une ou plusieurs informations a été incorrectement"
    #                 "saisie Veuiller ressaisir le information!"
    #         )
    #     self.assertEqual(response.redirect_chain[0][0], reverse('vote:create_voting'))

    # def test_post_with_voting_saved(self):
    #     self.client.post(
    #         '/vote/create_voting/', data=self.form_data, follow=True
    #     )
    #     new_voting = Voting.objects.all().order_by('-id')
    #     self.assertTrue(new_voting)
