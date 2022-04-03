"""Test delete voting view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from proposition.models.proposition import Proposition
from vote.models.voting_method import VotingMethod
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class DeletePropositionViewTest(TestCase):
    """Test DeletePropositionView class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/proposition/delete_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'proposition/delete_proposition.html'
        )
        self.assertIsInstance(response.context['proposition'], Proposition)

    def test_get_with_first_alternative_scenario(self):
        self.client.login(email='user2@email.com', password='yyy_Yyyy')
        response = self.client.get(
            '/proposition/delete_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('proposition:collectivity_propositions')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(
            response_msg.message, "Le créateur seulement peut "
            "supprimer la proposition"
        )

    def test_get_with_second_alternative_scenario(self):
        response = self.client.get(
            '/proposition/delete_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )

    def test_post_with_authenticated_user(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post('/proposition/delete_proposition/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('proposition:collectivity_propositions')
        )
        try:
            proposition = Proposition.objects.get(pk=1)
        except:
            proposition = False
        self.assertFalse(proposition)
        self.assertEqual(
            response.context['messages']._loaded_data[0].message, 
            "Suppression de proposition réussie"
        )
        self.assertEqual(
            response.context['messages']._loaded_data[0].level_tag, 
            "success"
        )

    def test_post_with_first_alternative_scenario(self):
        self.client.login(email='user2@email.com', password='yyy_Yyyy')
        response = self.client.post(
            '/proposition/delete_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('proposition:collectivity_propositions')
        )
        self.assertEqual(response_msg.level_tag, 'error')
        self.assertEqual(
            response_msg.message, "Le créateur seulement peut "
            "supprimer la proposition"
        )

    def test_post_with_second_alternative_scenario(self):
        response = self.client.post(
            '/proposition/delete_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )
