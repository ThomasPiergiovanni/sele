"""Proposition module model
"""
from django.db import models

from authentication.models import CustomUser
from proposition.models.category import Category
from proposition.models.creator_type import CreatorType
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.rating import Rating
from proposition.models.status import Status

class Proposition(models.Model):
    """Proposition class model
    """
    name = models.CharField(max_length=128, null=False)
    description = models.TextField(max_length=1000, null=False)
    creation_date =  models.DateTimeField(null=False)
    start_date =  models.DateField(null=False)
    end_date =  models.DateField(null=False)
    duration =  models.IntegerField(null=False)
    proposition_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False,
        related_name="proposition_category"
    )
    proposition_creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name="proposition_creator", null=False
    )
    proposition_creator_type = models.ForeignKey(
        CreatorType, on_delete=models.CASCADE, null=False,
        related_name="proposition_creator_type"
    )
    proposition_domain = models.ForeignKey(
        Domain, on_delete=models.CASCADE, null=False,
        related_name="proposition_domain"
    )
    proposition_kind = models.ForeignKey(
        Kind, on_delete=models.CASCADE, null=False,
        related_name="proposition_kind"
    )
    proposition_rating = models.ForeignKey(
        Rating, on_delete=models.CASCADE, null=False,
        related_name="proposition_rating"    
    )
    proposition_status = models.ForeignKey(
        Status, on_delete=models.CASCADE, null=False,
        related_name="proposition_status"
    )
    proposition_taker = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True,
        related_name="proposition_taker"
    )
    blocked_takers = models.ManyToManyField(
        CustomUser,
        through='BlockedTaker',
        related_name="blocked_takers"
    )
