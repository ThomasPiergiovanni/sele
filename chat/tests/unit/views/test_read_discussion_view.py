# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from chat.views.read_discussion_view import ReadDiscussionView


class ReadDiscussionViewTest(TestCase):

    def setUp(self):
        self.view = ReadDiscussionView()

    def test_init_with_read_discussion_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template, 'chat/read_discussion.html')
        self.assertEqual(
            ReadDiscussionView.login_url, '/authentication/login/'
        )
        self.assertEqual(ReadDiscussionView.redirect_field_name, None)
        self.assertIsNone(self.view.context['discussion'])
        self.assertTrue(self.view.context['form'])
        self.assertIsNone(self.view.context['comments'])
