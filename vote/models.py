# pylint: disable=E0307
"""Vote models module.
"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from authentication.models import CustomUser


class VotingMethod(models.Model):
    """VotingMethod model class.
    """

    name = models.CharField(max_length=32, unique=True)
    percentage = models.DecimalField(
        max_digits=3, decimal_places=2,
        validators=[MinValueValidator(0.01), MaxValueValidator(1)],
        unique=True
    )

    def __str__(self):
        return self.name


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
        CustomUser, through="Vote",  related_name="votes"
    )


class Vote(models.Model):
    """Vote model class.
    """

    choice = models.BooleanField(null=False)
    creation_date = models.DateTimeField()
    vote_voting = models.ForeignKey(
        Voting,
        on_delete=models.CASCADE,
        null=False,
        related_name="vote_voting"
    )
    vote_custom_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        related_name="vote_custom_user"
    )
