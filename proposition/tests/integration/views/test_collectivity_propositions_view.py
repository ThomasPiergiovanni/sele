"""Test collectivity propositions view module.
"""
from django.test import TestCase
from django.urls import reverse

from proposition.forms.collectivity_propositions_form import CollectivityPropositionsForm
from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import PropositionEmulation 


class CollectivityPropositionsViewTest(TestCase):
    """Test CollectivityPropositionsView class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_get_with_nominal_scenario(self):
        self.proposition_emulation.emulate_proposition()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/proposition/collectivity_propositions/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposition/propositions.html')
        self.assertIsInstance(response.context['page_objects'][0], Proposition)
        self.assertEqual(
            response.context['page_objects'][0].name,
            "Cours de Java"
        )
        self.assertEqual(
            response.context['page_objects'][0].proposition_category,
            Proposition.objects.get(pk=3).proposition_category
        )
    
    def test_get_with_alternative_scenario_one(self):
        self.proposition_emulation.emulate_proposition()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        session = self.client.session
        session['c_p_v_f_attribute'] = 'proposition_kind'
        session['c_p_v_f_order'] = 'asc'
        session.save()
        response = self.client.get(
            '/proposition/collectivity_propositions/', follow=True)
        self.assertEqual(
            response.context['page_objects'][0].name,
            "Cours de Python"
        )

    def test_get_with_alternative_scenario_two(self):
        response = self.client.get(
            '/proposition/collectivity_propositions/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            '/authentication/login/'
        )

    # def test_post_with_nominal_scenario(self):
    #     self.client.login(email='user1@email.com', password='xxx_Xxxx')
    #     form = {'attribute_selector': 'date', 'order_selector': 'asc'}
    #     response = self.client.post(
    #         '/vote/collectivity_votings/', data=form, follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'vote/votings.html')
    #     self.assertIsInstance(response.context['page_objects'][0], Voting)
    #     self.assertEqual(
    #         response.context['page_objects'][0].question,
    #         "Voulez-vous créer une demande de nettoyage?"
    #     )
    #     self.assertEqual(
    #         response.context['page_objects'][1].question,
    #         "Voulez-vous créer une demande de python?"
    #     )
    # def test_post_with_alternative_scenario_one_missing_input(self):
    #     self.client.login(email='user1@email.com', password='xxx_Xxxx')
    #     form = {'attribute_selector': '', 'order_selector': 'asc'}
    #     response = self.client.post(
    #         '/vote/collectivity_votings/', data=form, follow=True
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'vote/votings.html')
    #     self.assertIsInstance(response.context['page_objects'][0], Voting)
    #     self.assertEqual(
    #         response.context['page_objects'][0].question,
    #         "Voulez-vous créer une demande de python?"
    #     )
    #     self.assertEqual(
    #         response.context['page_objects'][1].question,
    #         "Voulez-vous créer une demande de nettoyage?"
    #     )
    #     self.assertTrue(response.context['form'].errors)

    # def test_post_with_alternative_scenario_two(self):
    #     form = {'attribute_selector': 'date', 'order_selector': 'asc'}
    #     response = self.client.post(
    #         '/vote/collectivity_votings/', data=form, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     response_msg = response.context['messages']._loaded_data[0]
    #     self.assertEqual(
    #         response.redirect_chain[0][0],reverse('information:home')
    #     )
    #     self.assertEqual(response_msg.level_tag, 'error')
    #     self.assertEqual(response_msg.message, "Authentification requise")