# pylint: disable=E0307
"""Collectivity model module.
"""
from django.contrib.gis.db import models

from collectivity.models.postal_code import PostalCode


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
