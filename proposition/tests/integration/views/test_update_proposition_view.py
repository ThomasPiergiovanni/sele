"""Test update proposition view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.tests.emulation.chat_emulation import ChatEmulation
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)

from proposition.models.proposition import Proposition
from vote.models.voting_method import VotingMethod


class UpdatePropositionViewTest(TestCase):
    """Test UpdatePropositionView class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_discussion()
        self.chat_emulation.emulate_comment()
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_proposition()

    def test_post_with_nominal_scenario_with_status_nouveau(self):
        self.client.login(email='user3@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/proposition/update_proposition/3/',
            data={'update_status_button': 'select'},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            '/proposition/collectivity_propositions/'
        )
        try:
            proposition = Proposition.objects.get(pk=3)
        except:
            proposition = False
        self.assertTrue(proposition)
        self.assertEqual(proposition.proposition_status.name, "Sélectionné")
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(response_msg.message,
            "Le statut de la proposition a été mis-à-jour"
        )
        self.assertEqual(response_msg.level_tag, "success")

    def test_post_with_nominal_scenario_with_status_not_exist(self):
        self.client.login(email='user3@email.com', password='xxx_Xxxx')
        response = self.client.post(
            '/proposition/update_proposition/3/',
            data={'update_status_button': 'fake'},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            '/proposition/collectivity_propositions/'
        )
        try:
            proposition = Proposition.objects.get(pk=3)
        except:
            proposition = False
        self.assertTrue(proposition)
        self.assertEqual(proposition.proposition_status.name, "Nouveau")
