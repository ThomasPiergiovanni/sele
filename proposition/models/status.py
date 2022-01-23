from django.db import models


class Status(models.Model):
    """Status class model
    """
    name = models.CharField(max_length=16, unique=True)
