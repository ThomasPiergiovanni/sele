# pylint: disable=E0307
"""Collectivity models module.
"""
from django.contrib.gis.db import models


class PostalCode(models.Model):
    """PostalCode model class.
    """
    postal_code = models.CharField(max_length=5, unique=False)
    insee_code = models.CharField(max_length=5, unique=False, default=None)

    def __str__(self):
        return self.postal_code

class Collectivity(models.Model):
    """Collectivity model class.
    """
    name = models.CharField('Nom', max_length=256)
    insee_code = models.CharField('Code INSEE', max_length=5)
    activity = models.CharField('Groupe actif', max_length=3)
    feat_geom = models.MultiPolygonField()
    postal_code = models.ForeignKey(
        PostalCode, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name
