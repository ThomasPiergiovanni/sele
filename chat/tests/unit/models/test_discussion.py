"""Test discussion method module.
"""
from datetime import date
from django.db import models
from django.test import TestCase
from django.utils import timezone

from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from chat.models.discussion import Discussion


class DiscussionTest(TestCase):
    """Test discussion class.
    """
    def setUp(self):
        self.emulate_discussion()

    def emulate_discussion(self):
        """
        """
        CustomUserTest().emulate_custom_user()
        Discussion.objects.create(
            id=1,
            subject="Travail avec asso Santé",
            creation_date=datetime(
                2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
            ),
            discussion_custom_user=1
        ),
        Discussion.objects.create(
            id=2,
            subject="Construction en brique",
            creation_date=datetime(
                2022, 1, 20, 17, 10, 38, tzinfo=timezone.utc
            ),
            discussion_custom_user=2
        )

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
        attribute = Discussion._meta.get_field('custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, models.CASCADE))
        )
    
    def test_question_with_emulated_question_instance(self):
        discussion = Discussion.objects.get(pk=1)
        self.assertEqual(discussion.subject, "Travail avec asso Santé")
        self.assertEqual(discussion.creation_date, date(
            2022, 1, 20,)
        )
        discussion = Discussion.objects.get(pk=2)
        self.assertEqual(discussion.subject, "Construction en brique")
        self.assertEqual(discussion.creation_date, date(
            2022, 1, 20)
        )
