from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Rating(models.Model):
    """Rating class model
    """
    rate = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
