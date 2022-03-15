"""Test delete voting view module.
"""
from django.test import TestCase

from vote.forms.voting_form import VotingForm
from vote.views.delete_voting_view import DeleteVotingView

class TestDeleteVotingView(TestCase):
    """Test DeleteVotingView class.
    """
    def setUp(self):
        self.view = DeleteVotingView()

    def test_init_with_create_voting_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'vote/detailed_voting.html')
        self.assertEqual(
            self.view.alternative_one_view_name, 'vote:overview'
        )
        self.assertEqual(
            self.view.alternative_two_view_name, 'information:home'
        )
        self.assertIsNone(self.view.context['voting'])
        self.assertIsNone(self.view.context['voting_status'])
        self.assertIsNone(self.view.context['voting_operation'])
        self.assertIsNone(self.view.context['voting_result'])
