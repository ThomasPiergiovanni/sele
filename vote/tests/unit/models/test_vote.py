"""Test vote module.
"""
from datetime import datetime

from django.db import models
from django.test import TestCase
from django.utils import timezone

from authentication.models import CustomUser

from vote.tests.emulation.vote_emulation import VoteEmulation
from vote.models.vote import Vote
from vote.models.voting import Voting



class VoteTest(TestCase):
    """Test vote class.
    """
    def setUp(self):
        self.vote_emulation = VoteEmulation()
    
    def test_vote_with_vote_class(self):
        self.vote_emulation.emulate_vote()
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
        attribute = Vote._meta.get_field('vote_voting')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),type(models.ForeignKey(Voting, models.CASCADE))
        )
    def test_vote_with_attr_custom_user_id_characteristic(self):
        attribute = Vote._meta.get_field('vote_custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, models.CASCADE))
        )
    
    def test_status_with_emulated_status_instance(self):
        self.vote_emulation.emulate_vote()
        vote = Vote.objects.get(pk=1)
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
