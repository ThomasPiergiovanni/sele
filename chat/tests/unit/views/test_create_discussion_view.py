# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from chat.forms.discussion_form import DiscussionForm
from chat.views.create_discussion_view import CreateDiscussionView


class CreateDiscussionViewTest(TestCase):

    def setUp(self):
        self.view = CreateDiscussionView()

    def test_init_with_create_voting_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(
            self.view.view_template, 'chat/create_discussion.html'
        )
        self.assertEqual(
            CreateDiscussionView.login_url, '/authentication/login/'
        )
        self.assertEqual(CreateDiscussionView.redirect_field_name, None)
        self.assertEqual(
            self.view.post_view_name, 'chat:collectivity_discussions'
        )
        self.assertIsInstance(self.view.context['form'], DiscussionForm)
