"""Blocked taker module
"""
from django.db import models

from authentication.models import CustomUser
from proposition.models.proposition import Proposition

class BlockedTaker(models.Model):
    """BlockedTaker class model
    """
    blocked_taker_custom_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False,
        related_name= 'blocked_taker_custom_user'
    )
    blocked_taker_proposition = models.ForeignKey(
        Proposition, on_delete=models.CASCADE, null=False,
        related_name= 'blocked_taker_proposition'
    )
