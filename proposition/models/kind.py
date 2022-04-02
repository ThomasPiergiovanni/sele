from django.db import models


class Kind(models.Model):
    """Kind class model
    """
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name