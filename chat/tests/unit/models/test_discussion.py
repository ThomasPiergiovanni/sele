# pylint: disable=C0114,C0115,C0116,E1101,R0201,W0212
from datetime import date

from django.db import models
from django.test import TestCase

from authentication.models import CustomUser
from chat.models import Discussion, DiscussionType
from chat.tests.emulation.chat_emulation import ChatEmulation


class DiscussionTest(TestCase):
    """Test discussion class.
    """
    def setUp(self):
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_test_setup()

    def test_discussion_with_discussion_class(self):
        discussion = Discussion.objects.get(pk=1)
        self.assertIsInstance(discussion, Discussion)

    def test_discussion_with_attr_subject_characteristic(self):
        attribute = Discussion._meta.get_field('subject')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 256)
        self.assertEqual(attribute.unique, False)

    def test_discussion_with_attr_creation_date_characteristic(self):
        attribute = Discussion._meta.get_field('creation_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateField()))

    def test_question_with_attr_custom_user_characteristic(self):
        attribute = Discussion._meta.get_field('discussion_custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, models.CASCADE))
        )

    def test_question_with_attr_discussion_discu_type_characteristic(self):
        attribute = Discussion._meta.get_field('discussion_discussion_type')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(DiscussionType, on_delete=models.CASCADE))
        )

    def test_question_with_emulated_question_instance(self):
        discussion = Discussion.objects.get(pk=1)
        self.assertEqual(discussion.subject, "Sujet est HTML")
        self.assertEqual(discussion.creation_date, date(
            2022, 1, 20,)
        )
        discussion = Discussion.objects.get(pk=2)
        self.assertEqual(discussion.subject, "Sujet est CSS")
        self.assertEqual(discussion.creation_date, date(
            2022, 1, 21)
        )
