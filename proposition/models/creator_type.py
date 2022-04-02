from django.db import models


class CreatorType(models.Model):
    """Creator type class model
    """
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name
