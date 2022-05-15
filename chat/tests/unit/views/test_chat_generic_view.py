# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from chat.management.engine.manager import Manager
from chat.views.generic_chat_view import GenericChatView


class ChatGenericViewTest(TestCase):

    def setUp(self):
        self.view = GenericChatView()

    def test_init_with_overview_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(GenericChatView.login_url, '/authentication/login/')
        self.assertEqual(GenericChatView.redirect_field_name, None)
        self.assertIsInstance(self.view.manager, Manager)
