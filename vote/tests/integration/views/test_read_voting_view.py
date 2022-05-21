# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase
from django.urls import reverse

from vote.models.voting import Voting
from vote.tests.emulation.vote_emulation import VoteEmulation


class ReadVotingViewTest(TestCase):

    def setUp(self):
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_test_setup()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/read_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/read_voting.html')
        self.assertIsInstance(response.context['voting'], Voting)
        self.assertEqual(response.context['voting_status'], 'Ouvert')
        self.assertEqual(response.context['voting_operation'], 'read')
        self.assertEqual(response.context['voting_result'], 50)

    def test_get_with_alternative_scenario(self):
        response = self.client.get('/vote/read_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
