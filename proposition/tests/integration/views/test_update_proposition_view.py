"""Test update proposition view module.
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


class UpdatePropositionViewTest(TestCase):
    """Test UpdatePropositionView class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_proposition()


    def test_post_with_nominal_scenario_with_status_nouveau(self):
        self.client.login(email='user3@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/proposition/update_proposition/4/',
            data={
                'update_status_button': 'select'
            },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], '/proposition/read_proposition/4/'
        )
        try:
            proposition = Proposition.objects.get(pk=4)
        except:
            proposition = False
        self.assertTrue(proposition)
        self.assertEqual(proposition.proposition_status.name, "Sélectionné")
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(response_msg.message, "Statut mis-à-jour")
        self.assertEqual(response_msg.level_tag, "success")

    # def test_post_with_alternative_scenario_one_with_status_annule(self):
    #     self.client.login(email='user1@email.com', password='xxx_Xxxx')
    #     response = self.client.post(
    #         '/proposition/delete_proposition/1/', follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     try:
    #         proposition = Proposition.objects.get(pk=1)
    #     except:
    #         proposition = False
    #     self.assertTrue(proposition)
    #     self.assertEqual(
    #         response.redirect_chain[0][0],
    #         reverse('proposition:collectivity_propositions')
    #     )
    #     response_msg = response.context['messages']._loaded_data[0]
    #     self.assertEqual(response_msg.level_tag, 'warning')
    #     self.assertEqual(
    #         response_msg.message,
    #         "Une proposition avec ce satut ne peut pas être supprimée"
    #     )

    # def test_post_with_alternative_scenario_two_with_status_en_cours(self):
    #     self.client.login(email='user2@email.com', password='yyy_Yyyy')
    #     response = self.client.post(
    #         '/proposition/delete_proposition/2/', follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     try:
    #         proposition = Proposition.objects.get(pk=2)
    #     except:
    #         proposition = False
    #     self.assertTrue(proposition)
    #     self.assertEqual(proposition.proposition_status.name, 'Annulé')
    #     response_msg = response.context['messages']._loaded_data[0]
    #     self.assertEqual(
    #         response.redirect_chain[0][0],
    #         reverse('proposition:collectivity_propositions')
    #     )
    #     self.assertEqual(response_msg.message, "Suppression réussie")
    #     self.assertEqual(response_msg.level_tag, "success")

    # def test_post_with_alternative_scenario_three_with_status_not_creator(self):
    #     self.client.login(email='user2@email.com', password='yyy_Yyyy')
    #     response = self.client.post(
    #         '/proposition/delete_proposition/1/', follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     response_msg = response.context['messages']._loaded_data[0]
    #     self.assertEqual(
    #         response.redirect_chain[0][0],
    #         reverse('proposition:collectivity_propositions')
    #     )
    #     self.assertEqual(response_msg.level_tag, 'error')
    #     self.assertEqual(
    #         response_msg.message, "Le créateur seulement peut "
    #         "supprimer la proposition"
    #     )

    # def test_post_with_alternative_scenario_four(self):
    #     response = self.client.post(
    #         '/proposition/delete_proposition/1/', follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(
    #         response.redirect_chain[0][0],reverse('authentication:login')
    #     )
