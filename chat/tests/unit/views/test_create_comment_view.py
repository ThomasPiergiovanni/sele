"""Test create comment view module.
"""
from django.test import TestCase

from chat.views.create_comment_view import CreateCommentView

class CreateCommentViewTest(TestCase):
    """Test CreateCommentView class.
    """
    def setUp(self):
        self.view = CreateCommentView()

    def test_init_with_create_comment_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_name,'chat:read_discussion')
        self.assertEqual(
            CreateCommentView.login_url , '/authentication/login/'
        )
        self.assertEqual(
            CreateCommentView.redirect_field_name , None
        )
