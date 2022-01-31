"""Test vote module.
"""
from datetime import datetime

from django.db import models
from django.test import TestCase
from django.utils import timezone

from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from vote.models.vote import Vote
from vote.models.voting import Voting
from vote.tests.unit.models.test_voting import VotingTest


class VoteTest(TestCase):
    """Test vote class.
    """
    def setUp(self):
        self.emulate_vote()

    def emulate_vote(self):
        """
        """
        CustomUserTest().emulate_custom_user()
        VotingTest().emulate_voting()
        Vote.objects.create(
            id=1,
            choice=True,
            creation_date=datetime(
                2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
            ), 
            voting_id=1,
            custom_user_id=1,
        ),
        Vote.objects.create(
            id=2,
            choice=False,
            creation_date=datetime(
                2022, 1, 20, 17, 10, 38, tzinfo=timezone.utc
            ), 
            voting_id=1,
            custom_user_id=2,
        )

    def test_vote_with_vote_class(self):
        vote = Vote.objects.get(pk=1)
        self.assertIsInstance(vote, Vote)

    def test_vote_with_attr_choice_characteristic(self):
        attribute = Vote._meta.get_field('choice')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.BooleanField()))
        self.assertEqual(attribute.null, False)

    def test_vote_with_attr_creation_date_characteristic(self):
        attribute = Vote._meta.get_field('creation_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateTimeField()))

    def test_vote_with_attr_voting_id_characteristic(self):
        attribute = Vote._meta.get_field('voting')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),type(models.ForeignKey(Voting, models.CASCADE))
        )
    def test_vote_with_attr_custom_user_id_characteristic(self):
        attribute = Vote._meta.get_field('custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, models.CASCADE))
        )
    
    def test_status_with_emulated_status_instance(self):
        vote= Vote.objects.get(pk=1)
        self.assertEqual(vote.choice, True)
        self.assertEqual(
            vote.creation_date,
            datetime(2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc)
        )
        vote= Vote.objects.get(pk=2)
        self.assertEqual(vote.choice, False)
        self.assertEqual(
            vote.creation_date, 
            datetime(2022, 1, 20, 17, 10, 38, tzinfo=timezone.utc)
        )
