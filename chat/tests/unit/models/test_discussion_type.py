# pylint: disable=C0114,C0115,C0116,E1101,R0201,W0212
from django.db import models
from django.test import TestCase

from chat.tests.emulation.chat_emulation import ChatEmulation
from chat.models.discussion_type import DiscussionType


class DiscussionTypeTest(TestCase):

    def setUp(self):
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_test_setup()

    def test_status_with_status_class(self):
        discussion_type = DiscussionType.objects.get(pk=1)
        self.assertIsInstance(discussion_type, DiscussionType)

    def test_status_with_status_attr_name_characteristic(self):
        attribute = DiscussionType._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 32)
        self.assertEqual(attribute.unique, True)

    def test_status_with_emulated_status_instance(self):
        discussion_type = DiscussionType.objects.get(pk=1)
        self.assertEqual(discussion_type.name, "Proposition")
        self.assertEqual(discussion_type.__str__(), "Proposition")
        discussion_type = DiscussionType.objects.get(pk=2)
        self.assertEqual(discussion_type.name, "Votation")
