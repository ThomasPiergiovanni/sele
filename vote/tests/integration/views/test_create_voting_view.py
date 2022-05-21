# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase
from django.urls import reverse

from vote.forms.voting_form import VotingForm
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.emulation.vote_emulation import VoteEmulation


class CreateVotingViewTest(TestCase):

    def setUp(self):
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_test_setup()
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

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/vote/create_voting/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/create_voting.html')
        self.assertIsInstance(response.context['form'], VotingForm)

    def test_get_with_alternative_scenario(self):
        response = self.client.get('/vote/create_voting/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )

    def test_post_with_nominal_scenario(self):
        Voting.objects.all().delete()
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
            response.redirect_chain[0][0], reverse('vote:collectivity_votings')
        )
        self.assertEqual(response_msg.level_tag, 'success')
        self.assertEqual(response_msg.message, "Création réussie")

    def test_post_with_alternative_scenario_with_wrong_form(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/vote/create_voting/', data=self.wrong_form_data, follow=True
        )
        self.assertTemplateUsed(response, 'vote/create_voting.html')
        self.assertIsInstance(response.context['form'], VotingForm)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_alternative_scenario_with_unauthenticated_user(self):
        response = self.client.post(
            '/vote/create_voting/', data=self.form_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
