"""Test create vote view module.
"""
from django.test import TestCase

from vote.forms.voting_form import VotingForm
from vote.views.delete_voting_view import CreateVoteView

class CreateVoteViewTest(TestCase):
    """Test CreateVoteView class.
    """
    def setUp(self):
        self.view = CreateVoteView()

    def test_init_with_create_voting_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'vote/create_vote.html')
        self.assertEqual(
            self.view.alternative_one_view_name, 'vote:detailed_voting'
        )
        self.assertEqual(
            self.view.alternative_two_view_name, 'information:home'
        )
        self.assertIsNone(self.view.context['voting'])
        self.assertEqual(
            self.view.msg_unauthenticated, "Authentification requise"
        )
        self.assertEqual(
            self.view.msg_already_voted,
            "Vous avez déja voté"
        )
        self.assertEqual(
            self.view.msg_post_success,"A voté!"
        )
