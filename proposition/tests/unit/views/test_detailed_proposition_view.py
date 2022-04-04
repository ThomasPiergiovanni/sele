"""Test detailed proposition view module.
"""
from django.test import TestCase

from proposition.views.detailed_proposition_view import DetailedPropositionView

class DetailedPropositionViewTest(TestCase):
    """TestDetailedPropositionView class.
    """
    def setUp(self):
        self.view = DetailedPropositionView()

    def test_init_with_deatile_voting_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'proposition/detailed_proposition.html')
        self.assertEqual(
            DetailedPropositionView.login_url , '/authentication/login/'
        )
        self.assertEqual(DetailedPropositionView.redirect_field_name, None)
        self.assertIsNone(self.view.context['proposition'])
        self.assertIsNone(self.view.context['proposition_operation'])
