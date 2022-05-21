# pylint: disable=E0307
"""CreatorType model module.
"""
from django.db import models


class CreatorType(models.Model):
    """CreatorType type model class.
    """

    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name
