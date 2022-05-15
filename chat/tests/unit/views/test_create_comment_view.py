# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from chat.views.create_comment_view import CreateCommentView


class CreateCommentViewTest(TestCase):

    def setUp(self):
        self.view = CreateCommentView()

    def test_init_with_create_comment_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_name, 'chat:read_discussion')
        self.assertEqual(
            CreateCommentView.login_url, '/authentication/login/'
        )
        self.assertEqual(
            CreateCommentView.redirect_field_name, None
        )
