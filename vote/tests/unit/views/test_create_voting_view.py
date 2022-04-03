"""Test create voting view view module.
"""
from django.test import TestCase

from vote.forms.voting_form import VotingForm
from vote.views.create_voting_view import CreateVotingView


class CreateVotingViewTest(TestCase):
    """Test CreateVotingView class.
    """
    def setUp(self):
        self.view = CreateVotingView()

    def test_init_with_create_voting_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'vote/create_voting.html')
        self.assertEqual(
            CreateVotingView.login_url , '/authentication/login/'
        )
        self.assertEqual(CreateVotingView.redirect_field_name , None)
        self.assertEqual(self.view.post_view_name, 'vote:collectivity_votings')
        self.assertIsInstance(self.view.context['form'], VotingForm)
