"""Test read proposition view module.
"""
from django.test import TestCase
from django.urls import reverse

from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)

class ReadPropositionViewTest(TestCase):
    """Test ReadPropositionView class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_get_with_nominal_scenario(self):
        self.proposition_emulation.emulate_proposition()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/proposition/read_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposition/read_proposition.html')
        self.assertIsInstance(response.context['proposition'], Proposition)
        self.assertEqual(response.context['proposition_operation'], 'read')

    def test_get_with_alternative_scenario(self):
        self.proposition_emulation.emulate_proposition()
        response = self.client.get(
            '/proposition/read_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )
