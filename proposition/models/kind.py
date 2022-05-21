# pylint: disable=E0307
"""Kind model module.
"""
from django.db import models


class Kind(models.Model):
    """Kind model class.
    """

    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name
