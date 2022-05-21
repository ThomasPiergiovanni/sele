"""Voting model module.
"""
from django.db import models

from authentication.models import CustomUser
from vote.models.vote import Vote
from vote.models.voting_method import VotingMethod


class Voting(models.Model):
    """Voting model class.
    """

    question = models.CharField(max_length=256, unique=False)
    description = models.TextField(max_length=1000)
    creation_date = models.DateField()
    opening_date = models.DateField()
    closure_date = models.DateField()
    voting_method = models.ForeignKey(
        VotingMethod, on_delete=models.CASCADE, related_name="voting_method"
    )
    voting_custom_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="voting_custom_user"
    )
    votes = models.ManyToManyField(
        CustomUser, through=Vote,  related_name="votes"
    )
