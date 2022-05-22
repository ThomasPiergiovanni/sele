# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase
from django.urls import reverse

from vote.models import Vote, Voting
from vote.tests.emulation.vote_emulation import VoteEmulation


class CreateVoteView(TestCase):

    def setUp(self):
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_test_setup()

    def test_get_with_nominal_scenario(self):
        Vote.objects.all().delete()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/create_vote/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/create_vote.html')
        self.assertIsInstance(response.context['voting'], Voting)

    def test_get_with_first_alternative_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/create_vote/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('vote:read_voting', args=[1])
        )
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(message.message, "Vous avez déja voté")

    def test_get_with_second_alternative_scenario(self):
        response = self.client.get('/vote/create_vote/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )

    def test_post_with_nominal_scenario_vote_yes(self):
        Vote.objects.all().delete()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/vote/create_vote/1/', data={'form_vote': 'yes'}, follow=True
        )
        try:
            vote = Vote.objects.all().last()
        except Vote.DoesNotExist:
            vote = False
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('vote:read_voting', args=[1])
        )
        self.assertTrue(vote)
        self.assertTrue(vote.choice)
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'success')
            self.assertEqual(message.message, "A voté!")

    def test_post_with_nominal_scenario_vote_no(self):
        Vote.objects.all().delete()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/vote/create_vote/1/', data={'form_vote': 'no'}, follow=True
        )
        try:
            vote = Vote.objects.get(pk=1)
        except Vote.DoesNotExist:
            vote = False
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('vote:read_voting', args=[1])
        )
        self.assertTrue(vote)
        self.assertFalse(vote.choice)
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'success')
            self.assertEqual(message.message, "A voté!")

    def test_post_with_first_alternative_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/vote/create_vote/1/', data={'form_vote': 'yes'}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('vote:read_voting', args=[1])
        )
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(message.message, "Vous avez déja voté")

    def test_post_with_second_alternative_scenario(self):
        Vote.objects.all().delete()
        response = self.client.post(
            '/vote/create_vote/1/', data={'form_vote': 'yes'}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
