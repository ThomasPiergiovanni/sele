# pylint: disable=E0307
"""Discussion type model module.
"""
from django.db import models


class DiscussionType(models.Model):
    """Discussion type model class.
    """

    name = models.CharField(max_length=32, unique=True, default=None)

    def __str__(self):
        return self.name
