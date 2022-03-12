"""Test reset vote module.
"""
from django.db import models
from django.test import TestCase

from vote.management.commands.reset_vote import Command
from vote.models.vote import Vote
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.emulation.vote_emulation import VoteEmulation


class ResetVoteTest(TestCase):
    """Test reset vote method class.
    """
    def setUp(self):
        """Method that set up data for the entire class
        """
        self.command = Command()
        self.vote_emulation = VoteEmulation()

    def test_drop_voting_method_with_instance_is_none(self):
        self.vote_emulation.emulate_voting_method()
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

    def test_drop_voting_with_instance_is_none(self):
        self.vote_emulation.emulate_voting()
        votings = Voting.objects.all()
        self.assertTrue(votings)
        self.command._Command__drop_voting()
        votings = Voting.objects.all()
        self.assertFalse(votings)
    
    def test_drop_vote_with_instance_is_none(self):
        self.vote_emulation.emulate_vote()
        vote = Vote.objects.all()
        self.assertTrue(vote)
        self.command._Command__drop_vote()
        vote = Vote.objects.all()
        self.assertFalse(vote)
