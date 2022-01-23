from django.db import models


class Domain(models.Model):
    """Domain class model
    """
    name = models.CharField(max_length=128, unique=True)
