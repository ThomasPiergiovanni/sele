from django.contrib.gis.db import models


class Collectivity(models.Model):
    name = models.CharField('Nom', max_length=256)
    insee_code = models.CharField('Code INSEE', max_length=5)
    activity = models.CharField('Groupe actif', max_length=3)
    feat_geom = models.MultiPolygonField()

    def __str__(self):
        return self.name
