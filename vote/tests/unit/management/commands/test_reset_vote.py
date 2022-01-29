"""Test reset vote module.
"""
from django.db import models
from django.test import TestCase

from vote.management.commands.reset_vote import Command
from vote.models.voting_method import VotingMethod
from vote.tests.unit.models.test_voting_method import VotingMethodTest


class ResetVoteTest(TestCase):
    """Test reset vote method class.
    """
    def setUp(self):
        """Method that set up data for the entire class
        """
        self.command = Command()

    def test_drop_voting_method_with_instance_is_none(self):
        VotingMethodTest().emulate_voting_method()
        voting_methods = VotingMethod.objects.all()
        self.assertTrue(voting_methods)
        self.command._Command__drop_voting_method()
        voting_methods = VotingMethod.objects.all()
        self.assertFalse(voting_methods)

    def test_insert_voting_method_with_instances_is_not_none(self):
        voting_methods = VotingMethod.objects.all()
        self.assertFalse(voting_methods)
        self.command._Command__insert_voting_method()
        voting_methods = VotingMethod.objects.all()
        self.assertTrue(voting_methods)
