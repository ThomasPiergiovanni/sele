from django.db import models

from authentication.models import CustomUser
from vote.models.voting import Voting


class Vote(models.Model):
    """Vote class model
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
