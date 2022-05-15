# pylint: disable=E0307
"""PostalCode model module.
"""
from django.db import models


class PostalCode(models.Model):
    """PostalCode model class.
    """
    postal_code = models.CharField(max_length=5, unique=False)
    insee_code = models.CharField(max_length=5, unique=False, default=None)

    def __str__(self):
        return self.postal_code
