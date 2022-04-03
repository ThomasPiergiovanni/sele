"""Test detailed voting view module.
"""
from django.test import TestCase

from vote.views.detailed_voting_view import DetailedVotingView

class DetailedVotingViewTest(TestCase):
    """TestDetailedVotingView class.
    """
    def setUp(self):
        self.view = DetailedVotingView()

    def test_init_with_deatile_voting_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'vote/detailed_voting.html')
        self.assertEqual(
            DetailedVotingView.login_url , '/authentication/login/'
        )
        self.assertEqual(DetailedVotingView.redirect_field_name, None)
        self.assertIsNone(self.view.context['voting'])
        self.assertIsNone(self.view.context['voting_status'])
        self.assertIsNone(self.view.context['voting_operation'])
        self.assertIsNone(self.view.context['voting_result'])
