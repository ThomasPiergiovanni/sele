from django.db import models

from vote.models.voting_method import VotingMethod


class Voting(models.Model):
    """Voting class model
    """
    question = models.CharField(max_length=256, unique=False)
    description = models.TextField(max_length=1000)
    creation_date = models.DateField()
    opening_date = models.DateField()
    closure_date = models.DateField()
    voting_method = models.ForeignKey(VotingMethod, models.CASCADE)

