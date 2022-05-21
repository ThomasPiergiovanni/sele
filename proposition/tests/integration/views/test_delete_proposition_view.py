# pylint: disable=C0114,C0115,C0116,E1101,W0212,R0801
from django.test import TestCase
from django.urls import reverse

from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class DeletePropositionViewTest(TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_test_setup()

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
            response.redirect_chain[0][0], reverse('authentication:login')
        )

    def test_post_with_nominal_scenario_with_status_nouveau(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/proposition/delete_proposition/3/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('proposition:collectivity_propositions')
        )
        try:
            proposition = Proposition.objects.get(pk=3)
        except Proposition.DoesNotExist:
            proposition = False
        self.assertFalse(proposition)
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(response_msg.message, "Suppression réussie")
        self.assertEqual(response_msg.level_tag, "success")

    def test_post_with_alternative_scenario_one_with_status_annule(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/proposition/delete_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        try:
            proposition = Proposition.objects.get(pk=1)
        except Proposition.DoesNotExist:
            proposition = False
        self.assertTrue(proposition)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('proposition:collectivity_propositions')
        )
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(response_msg.level_tag, 'warning')
        self.assertEqual(
            response_msg.message,
            "Une proposition avec ce satut ne peut pas être supprimée"
        )

    def test_post_with_alternative_scenario_two_with_status_annule(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/proposition/delete_proposition/2/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        try:
            proposition = Proposition.objects.get(pk=2)
        except Proposition.DoesNotExist:
            proposition = False
        self.assertTrue(proposition)
        self.assertEqual(proposition.proposition_status.name, 'Annulé')
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('proposition:collectivity_propositions')
        )
        self.assertEqual(response_msg.message, "Suppression réussie")
        self.assertEqual(response_msg.level_tag, "success")

    def test_post_with_alter_scenario_three_with_status_not_creator(self):
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

    def test_post_with_alternative_scenario_four(self):
        response = self.client.post(
            '/proposition/delete_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
