"""Test collectivity votings view module.
"""
from django.test import TestCase
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


    # def test_get_with_alternative_scenario(self):
    #     response = self.client.get('/vote/detailed_voting/1/', follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     response_msg = response.context['messages']._loaded_data[0]
    #     self.assertEqual(
    #         response.redirect_chain[0][0],reverse('information:home')
    #     )
    #     self.assertEqual(response_msg.level_tag, 'error')
    #     self.assertEqual(response_msg.message, "Authentification requise")
