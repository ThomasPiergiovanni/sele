# pylint: disable=C0114,C0115,C0116,E1101,R0201,W0212
from django.test import TestCase

from chat.management.commands.reset_chat import Command
from chat.models import DiscussionType
from chat.tests.emulation.chat_emulation import (
    ChatEmulation
)


class ResetChatTest(TestCase):

    def setUp(self):
        self.command = Command()
        self.chat_emulation = ChatEmulation()

    def test_drop_discussion_type_with_instance_is_none(self):
        self.chat_emulation.emulate_discussion_type()
        discussions_type = DiscussionType.objects.all()
        self.assertTrue(discussions_type)
        self.command._Command__drop_discussion_type()
        discussions_type = DiscussionType.objects.all()
        self.assertFalse(discussions_type)

    def test_insert_discussion_type_with_instances_is_not_none(self):
        discussions_type = DiscussionType.objects.all()
        self.assertFalse(discussions_type)
        self.command._Command__insert_discussion_type()
        discussions_type = DiscussionType.objects.all()
        self.assertTrue(discussions_type)
