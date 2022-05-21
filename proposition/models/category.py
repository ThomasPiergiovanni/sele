# pylint: disable=E0307
"""Category model module.
"""
from django.db import models


class Category(models.Model):
    """Category model class.
    """

    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name
