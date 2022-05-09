"""Test detailed voting view module.
"""
from django.test import TestCase
from django.urls import reverse

from vote.models.voting import Voting

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from vote.tests.emulation.vote_emulation import VoteEmulation


class DetailedVotingViewTest(TestCase):
    """Test DetailedVotingView class.
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
        response = self.client.get('/vote/detailed_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/detailed_voting.html')
        self.assertIsInstance(response.context['voting'], Voting)
        self.assertEqual(response.context['voting_status'], 'Ouvert')
        self.assertEqual(response.context['voting_operation'], 'read')
        self.assertEqual(response.context['voting_result'], 50)

    def test_get_with_alternative_scenario(self):
        response = self.client.get('/vote/detailed_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )
