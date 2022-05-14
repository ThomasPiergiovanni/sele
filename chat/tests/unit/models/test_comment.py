"""Test discussion method module.
"""
from datetime import datetime

from django.db import models
from django.test import TestCase
from django.utils import timezone

from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.tests.emulation.chat_emulation import ChatEmulation
from chat.models.comment import Comment
from chat.models.discussion import Discussion


class CommentTest(TestCase):
    """Test comment class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_discussion()
        self.chat_emulation.emulate_comment()

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
        attribute = Comment._meta.get_field('comment_custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, on_delete=models.CASCADE))
        )

    def test_comment_with_attr_relation_custom_user_characteristic(self):
        attribute = Comment._meta.get_field('comment_discussion')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Discussion, models.CASCADE))
        )
    
    def test_question_with_emulated_question_instance(self):
        comment = Comment.objects.get(pk=1)
        self.assertEqual(comment.comment, "Comment vas-tu?")
        self.assertEqual(
            comment.creation_date,
            datetime(2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc)
        )
        comment = Comment.objects.get(pk=2)
        self.assertEqual(comment.comment, "Ca vas et toi?")
        self.assertEqual(
            comment.creation_date,
            datetime(2022, 1, 20, 17, 10, 38, tzinfo=timezone.utc)
        )
