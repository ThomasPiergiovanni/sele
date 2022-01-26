from django.db import models


class PostalCode(models.Model):
    """Postal code class model
    """
    postal_code = models.CharField(max_length=5, unique=False)
    insee_code = models.CharField(max_length=5, unique=False)