"""Test discussion method module.
"""
from datetime import datetime
from django.db import models
from django.test import TestCase
from django.utils import timezone

from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from chat.models.comment import Comment
from chat.models.discussion import Discussion
from chat.tests.unit.models.test_discussion import DiscussionTest


class CommentTest(TestCase):
    """Test comment class.
    """
    def setUp(self):
        self.emulate_comment()

    def emulate_comment(self):
        """
        """
        DiscussionTest().emulate_discussion()
        timezone.now()
        Comment.objects.create(
            id=1,
            comment="Comment vas-tu?",
            creation_date=datetime(
                2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
            ),
            custom_user_id=1,
            discussion_id=1
        ),
        Comment.objects.create(
            id=2,
            comment="Ca vas et toi?",
            creation_date=datetime(
                2022, 1, 20, 17, 10, 38, tzinfo=timezone.utc
            ),
            custom_user_id=2,
            discussion_id=1
        )

    def test_comment_with_discussion_class(self):
        comment = Comment.objects.get(pk=1)
        self.assertIsInstance(comment, Comment)

    def test_comment_with_attr_subject_characteristic(self):
        attribute = Comment._meta.get_field('comment')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 256)

    def test_comment_with_attr_creation_date_characteristic(self):
        attribute = Comment._meta.get_field('creation_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateTimeField()))

    def test_comment_with_attr_custom_user_characteristic(self):
        attribute = Comment._meta.get_field('custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, models.CASCADE))
        )

    def test_comment_with_attr_relation_custom_user_characteristic(self):
        attribute = Comment._meta.get_field('discussion')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Discussion, models.CASCADE))
        )
    
    def test_question_with_emulated_question_instance(self):
        comment = Comment.objects.get(pk=1)
        self.assertEqual(comment.comment, "Comment vas-tu?")
        self.assertEqual(
            comment.creation_date, datetime(
                2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
            )
        )
        comment = Comment.objects.get(pk=2)
        self.assertEqual(comment.comment, "Ca vas et toi?")
        self.assertEqual(
            comment.creation_date, datetime(
                2022, 1, 20, 17, 10, 38, tzinfo=timezone.utc
            )
        )
