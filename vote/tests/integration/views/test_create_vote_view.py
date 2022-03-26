"""Test create vote view module.
"""
from django.test import TestCase
from django.urls import reverse

from vote.models.vote import Vote
from vote.models.voting import Voting
from vote.tests.emulation.vote_emulation import VoteEmulation


class CreateVoteView(TestCase):
    """Test CreateVoteView class.
    """
    def setUp(self):
        self.vote_emulation = VoteEmulation()

    def test_get_with_nominal_scenario(self):
        self.vote_emulation.emulate_voting()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/create_vote/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/create_vote.html')
        self.assertIsInstance(response.context['voting'], Voting)

    def test_get_with_first_alternative_scenario(self):
        self.vote_emulation.emulate_vote()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/create_vote/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('vote:detailed_voting', args=[1])
        )
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(message.message, "Vous avez déja voté")

    def test_get_with_second_alternative_scenario(self):
        response = self.client.get('/vote/create_vote/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(response_msg.message, "Authentification requise")

    def test_post_with_nominal_scenario_vote_no(self):
        self.vote_emulation.emulate_voting()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/vote/create_vote/1/', data={'form_vote':'yes'}, follow=True
        )
        try:
            vote = Vote.objects.get(pk=1)
        except:
            vote = False
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('vote:detailed_voting', args=[1])
        )
        self.assertTrue(vote)
        self.assertTrue(vote.choice)
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'success')
            self.assertEqual(message.message, "A voté!")

    def test_post_with_nominal_scenario_vote_no(self):
        self.vote_emulation.emulate_voting()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/vote/create_vote/1/', data={'form_vote':'no'}, follow=True
        )
        try:
            vote = Vote.objects.get(pk=1)
        except:
            vote = False
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('vote:detailed_voting', args=[1])
        )
        self.assertTrue(vote)
        self.assertFalse(vote.choice)
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'success')
            self.assertEqual(message.message, "A voté!")
    
    def test_post_with_first_alternative_scenario(self):
        self.vote_emulation.emulate_vote()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/vote/create_vote/1/', data={'form_vote':'yes'}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('vote:detailed_voting', args=[1])
        )
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(message.message, "Vous avez déja voté")

    def test_post_with_second_alternative_scenario(self):
        response = self.client.post(
            '/vote/create_vote/1/', data={'form_vote':'yes'}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],reverse('information:home')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(response_msg.message, "Authentification requise")
