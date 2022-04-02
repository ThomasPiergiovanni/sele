"""Test create propsoition view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from proposition.forms.proposition_form import PropositionForm
from proposition.models.category import Category
from proposition.models.creator_type import CreatorType
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)
from vote.models.voting import Voting
from vote.tests.emulation.vote_emulation import VoteEmulation


class CreatePropositionViewTest (TestCase):
    """Test CreatePropositionView test  class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_category()
        self.proposition_emulation.emulate_creator_type()
        self.proposition_emulation.emulate_domain()
        self.proposition_emulation.emulate_kind()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/proposition/create_proposition/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposition/create_proposition.html')
        self.assertIsInstance(response.context['form'], PropositionForm)

    def test_get_with_alternative_scenario(self):
        response = self.client.get(
            '/proposition/create_proposition/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], '/authentication/login/'
        )

    def test_post_with_nominal_scenario(self):    
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {
            'name': 'Cours de Python',
            'description': 'dsdss',
            'proposition_kind': Kind.objects.get(pk=1).id,
            'proposition_category': Category.objects.get(pk=1).id,
            'proposition_domain': Domain.objects.get(pk=1).id,
            'proposition_creator_type' : CreatorType.objects.get(pk=1),
            'start_date': "2022-01-25",
            'end_date': "2022-01-30",
            'duration': 45
        }
        response = self.client.post(
            '/proposition/create_proposition/', data=form_data, follow=True
        )
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Proposition.objects.all().last().question, 'Cours de Python'
        )
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('proposition:collectivity_proposition')
        )
        self.assertEqual(response_msg.level_tag, 'success')
        self.assertEqual(response_msg.message, "Création réussie")

    # def test_post_with_nominal_scenario_vote_no(self):
    #     self.proposition_emulation.emulate_proposition()
    #     self.client.login(email='user1@email.com', password='xxx_Xxxx')
    #     response = self.client.post(
    #         '/vote/create_vote/1/', data={'form_vote':'no'}, follow=True
    #     )
    #     try:
    #         vote = Vote.objects.get(pk=1)
    #     except:
    #         vote = False
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(
    #         response.redirect_chain[0][0],
    #         reverse('vote:detailed_voting', args=[1])
    #     )
    #     self.assertTrue(vote)
    #     self.assertFalse(vote.choice)
    #     for message in response.context['messages']:
    #         self.assertEqual(message.level_tag, 'success')
    #         self.assertEqual(message.message, "A voté!")
    
    # def test_post_with_first_alternative_scenario(self):
    #     self.vote_emulation.emulate_vote()
    #     self.client.login(email='user1@email.com', password='xxx_Xxxx')
    #     response = self.client.post(
    #         '/vote/create_vote/1/', data={'form_vote':'yes'}, follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(
    #         response.redirect_chain[0][0],
    #         reverse('vote:detailed_voting', args=[1])
    #     )
    #     for message in response.context['messages']:
    #         self.assertEqual(message.level_tag, 'error')
    #         self.assertEqual(message.message, "Vous avez déja voté")

    # def test_post_with_second_alternative_scenario(self):
    #     response = self.client.post(
    #         '/vote/create_vote/1/', data={'form_vote':'yes'}, follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     response_msg = response.context['messages']._loaded_data[0]
    #     self.assertEqual(
    #         response.redirect_chain[0][0],reverse('information:home')
    #     )
    #     self.assertEqual(response_msg.level_tag, 'error')
    #     self.assertEqual(response_msg.message, "Authentification requise")
