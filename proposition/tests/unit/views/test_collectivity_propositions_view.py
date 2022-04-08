"""Test collectivity propositions view module.
"""
from django.test import TestCase

from proposition.forms.collectivity_propositions_form import (
    CollectivityPropositionsForm
)
from proposition.views.collectivity_propositions_view import (
    CollectivityPropositionsView
)

class CollectivityPropositionsViewTest(TestCase):
    """PropositionsVotingsViewTest class.
    """
    def setUp(self):
        self.login_url = CollectivityPropositionsView.login_url
        self.redirect_field_name = (
            CollectivityPropositionsView.redirect_field_name
        )
        self.view = CollectivityPropositionsView()

    def test_init_with_overview_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(
            self.view.view_template,'proposition/propositions.html'
        )
        self.assertIsInstance(
            self.view.context['form'], CollectivityPropositionsForm
        )
        self.assertIsNone(self.view.context['page_objects'])
        self.assertEqual(self.login_url, '/authentication/login/')
        self.assertIsNone(self.redirect_field_name)

