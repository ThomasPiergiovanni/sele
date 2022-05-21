# pylint: disable=E0307
"""Domain model module.
"""

from django.db import models


class Domain(models.Model):
    """Domain model class.
    """
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
