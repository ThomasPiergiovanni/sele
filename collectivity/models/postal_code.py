from django.db import models

from collectivity.models.collectivity import Collectivity


class PostalCode(models.Model):
    """Postal code class model
    """
    postal_code = models.CharField(max_length=5, unique=False)
    collectivity = models.ForeignKey(Collectivity, models.CASCADE, default=999999)

    def __str__(self):
        return self.postal_code
