# pylint: disable=E0307
"""VotingMethod model module.
"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class VotingMethod(models.Model):
    """VotingMethod model.class.
    """

    name = models.CharField(max_length=32, unique=True)
    percentage = models.DecimalField(
        max_digits=3, decimal_places=2,
        validators=[MinValueValidator(0.01), MaxValueValidator(1)],
        unique=True
    )

    def __str__(self):
        return self.name
