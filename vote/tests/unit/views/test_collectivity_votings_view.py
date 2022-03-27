"""Test collectivity votings view module.
"""
from django.test import TestCase

from vote.forms.collectivity_votings_form import CollectivityVotingsForm
from vote.views.collectivity_votings_view import CollectivityVotingsView

class CollectivityVotingsViewTest(TestCase):
    """CollectivityVotingsViewTest class.
    """
    def setUp(self):
        self.view = CollectivityVotingsView()

    def test_init_with_overview_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'vote/votings.html')
        self.assertEqual(
            self.view.alternative_view_name, 'information:home'
        )
        self.assertIsInstance(
            self.view.context['form'], CollectivityVotingsForm
        )
        self.assertIsNone(self.view.context['page_objects'])
        self.assertEqual(
            self.view.msg_unauthenticated, "Authentification requise"
        )
