# pylint: disable=C0116, E1101
"""Test add voting view module.
"""
from django.test import TestCase
from django.urls import reverse

from vote.forms.voting_form import VotingForm
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.unit.models.test_voting import VotingTest
from vote.tests.unit.models.test_voting_method import VotingMethodTest


class CreateVotingTest(TestCase):
    """Test CreateVoting view class.
    """
    def setUp(self):
        VotingMethodTest().emulate_voting_method()
        Voting.objects.create(
            id=98,
            question="Voulez-vous créer une demande de nettoyage?",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date = "2022-01-10",
            opening_date = "2022-01-11",
            closure_date = "2022-01-19",
            voting_method_id=1
        )
        Voting.objects.create(
            id=99,
            question="Voulez-vous créer une demande de nettoyage?",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date = "2022-01-10",
            opening_date = "2022-01-11",
            closure_date = "2022-01-19",
            voting_method_id=1
        )
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

    def test_get_with_status_code_200(self):
        response = self.client.get('/vote/create_voting/')
        self.assertEqual(response.status_code, 200)

    def test_get_with_get_template(self):
        response = self.client.get('/vote/create_voting/')
        self.assertTemplateUsed(response, 'vote/create_voting.html')

    def test_get_with_voting_form(self):
        response = self.client.get('/vote/create_voting/')
        self.assertIsInstance(response.context['voting_form'], VotingForm)

    def test_post_with_status_code_200(self):
        response = self.client.post(
            '/vote/create_voting/', data=self.form_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
    
    def test_post_with_valid_response_redirect(self):
        response = self.client.post(
            '/vote/create_voting/', data=self.form_data, follow=True
        )
        self.assertEqual(response.redirect_chain[0][0], reverse('vote:overview'))

    def test_post_with_invalid_response(self):
        response = self.client.post(
            '/vote/create_voting/', data=self.wrong_form_data, follow=True
        )
        for message in response.context['messages']:
            self.assertEqual(message.level_tag, 'error')
            self.assertEqual(
                message.message, 
                "Une ou plusieurs informations a été incorrectement"
                    "saisie Veuiller ressaisir le information!"
            )
        self.assertEqual(response.redirect_chain[0][0], reverse('vote:create_voting'))

    def test_post_with_voting_saved(self):
        self.client.post(
            '/vote/create_voting/', data=self.form_data, follow=True
        )
        new_voting = Voting.objects.all().order_by('-id')
        self.assertTrue(new_voting)
