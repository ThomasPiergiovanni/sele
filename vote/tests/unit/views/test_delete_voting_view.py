# pylint: disable=C0114,C0115,C0116,E1101
from django.test import TestCase

from vote.views.delete_voting_view import DeleteVotingView


class DeleteVotingViewTest(TestCase):

    def setUp(self):
        self.view = DeleteVotingView()

    def test_init_with_create_voting_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template, 'vote/delete_voting.html')
        self.assertEqual(
            self.view.alternative_one_view_name, 'vote:collectivity_votings'
        )
        self.assertEqual(
            DeleteVotingView.login_url, '/authentication/login/'
        )
        self.assertEqual(DeleteVotingView.redirect_field_name, None)
        self.assertIsNone(self.view.context['voting'])
        self.assertEqual(
            self.view.msg_not_owner,
            "Le créateur seulement peut supprimer la votation"
        )
        self.assertEqual(
            self.view.msg_post_success, "Suppression de votation réussie"
        )
