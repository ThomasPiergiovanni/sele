# pylint: disable=C0114,C0115,C0116,E1101,W0212,R0801
from django.test import TestCase
from django.urls import reverse

from vote.models import Voting
from vote.tests.emulation.vote_emulation import VoteEmulation


class DeleteVotingViewTest(TestCase):

    def setUp(self):
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_test_setup()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/delete_voting.html')
        self.assertIsInstance(response.context['voting'], Voting)

    def test_get_with_first_alternative_scenario(self):
        self.client.login(email='user2@email.com', password='yyy_Yyyy')
        response = self.client.get('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0], reverse('vote:collectivity_votings')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(
            response_msg.message, "Le créateur seulement peut "
            "supprimer la votation"
        )

    def test_get_with_second_alternative_scenario(self):
        response = self.client.get('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )

    def test_post_with_authenticated_user(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('vote:collectivity_votings')
        )
        try:
            voting = Voting.objects.get(pk=1)
        except Voting.DoesNotExist:
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
            response.redirect_chain[0][0], reverse('vote:collectivity_votings')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(
            response_msg.message, "Le créateur seulement peut "
            "supprimer la votation"
        )

    def test_post_with_second_alternative_scenario(self):
        response = self.client.post('/vote/delete_voting/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
