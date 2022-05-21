# pylint: disable=C0114,C0115,C0116,E1101
from django.test import TestCase

from vote.views.create_vote_view import CreateVoteView


class CreateVoteViewTest(TestCase):

    def setUp(self):
        self.view = CreateVoteView()

    def test_init_with_create_voting_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template, 'vote/create_vote.html')
        self.assertEqual(
            self.view.alternative_one_view_name, 'vote:read_voting'
        )
        self.assertEqual(
            CreateVoteView.login_url, '/authentication/login/'
        )
        self.assertEqual(
            CreateVoteView.redirect_field_name, None
        )
        self.assertIsNone(self.view.context['voting'])
        self.assertEqual(
            self.view.msg_already_voted,
            "Vous avez déja voté"
        )
        self.assertEqual(
            self.view.msg_post_success, "A voté!"
        )
