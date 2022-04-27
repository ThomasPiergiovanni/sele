"""Test collectivity propositions view module.
"""
from django.test import TestCase
from django.urls import reverse

from proposition.forms.collectivity_propositions_form import CollectivityPropositionsForm
from proposition.models.proposition import Proposition
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.tests.emulation.chat_emulation import ChatEmulation
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class CollectivityPropositionsViewTest(TestCase):
    """Test CollectivityPropositionsView class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_discussion()
        self.chat_emulation.emulate_comment()
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_proposition()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/proposition/collectivity_propositions/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposition/propositions.html')
        self.assertIsInstance(response.context['page_objects'][0], Proposition)
        self.assertEqual(
            response.context['page_objects'][0].name, "OCours17"
        )
        self.assertEqual(
            response.context['page_objects'][0].proposition_category,
            Proposition.objects.get(pk=3).proposition_category
        )
    
    def test_get_with_alternative_scenario_one(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        session = self.client.session
        session['c_p_v_f_search_input'] = 'DCours1'
        session.save()
        response = self.client.get(
            '/proposition/collectivity_propositions/', follow=True)
        self.assertEqual(
            response.context['page_objects'][0].id, 1
        )

    def test_get_with_alternative_scenario_two(self):
        response = self.client.get(
            '/proposition/collectivity_propositions/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], '/authentication/login/'
        )

    def test_post_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form = {'search_input': 'DCours1','cpf_search_button': 'yes'}
        response = self.client.post(
            '/proposition/collectivity_propositions/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposition/propositions.html')
        self.assertIsInstance(response.context['page_objects'][0], Proposition)
        self.assertEqual(response.context['page_objects'][0].id, 1)

    def test_post_with_alternative_scenario_one_missing_input(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form = {'search_input': '','cpf_search_button': 'yes'}
        response = self.client.post(
            '/proposition/collectivity_propositions/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposition/propositions.html')
        self.assertIsInstance(response.context['page_objects'][0], Proposition)
        self.assertEqual(response.context['page_objects'][0].id, 17)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_alternative_scenario_two_clear(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form = {'search_input': '', 'cpf_clear_button': 'yes'}
        response = self.client.post(
            '/proposition/collectivity_propositions/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposition/propositions.html')
        self.assertIsInstance(response.context['page_objects'][0], Proposition)
        self.assertEqual(response.context['page_objects'][0].id, 17)
        self.assertFalse(response.context['form'].errors)

    def test_post_with_alternative_scenario_three(self):
        form = {'search_input': 'Python','cpf_search_button': 'yes'}
        response = self.client.post(
            '/proposition/collectivity_propositions/', data=form, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], '/authentication/login/'
        )
