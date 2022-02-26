"""Test rating module.
"""
from django.contrib.gis.utils import LayerMapping
from pathlib import Path

from collectivity.models.collectivity import Collectivity
from collectivity.models.postal_code import PostalCode
from config.settings import BASE_DIR

class CollectivityEmulation():
    """Collectivity emulation class.
    """

    def emulate_postal_code(self):
        """
        """
        PostalCode.objects.create(
            id=1, postal_code='92340', insee_code='92014'
        )
        PostalCode.objects.create(
            id=2, postal_code='92220', insee_code='92007'
        )

    def emulate_collectivity(self):
        """
        """
        collectivity_mapping = {
            'name': 'nom',
            'insee_code': 'insee',
            'activity': 'activity',
            'feat_geom': 'Polygon',
        }
        blr_layer = (
            Path(BASE_DIR).resolve().parent/'config/settings/data/'
            'bourg_la_reine.geojson'
        )
        bag_layer = (
            Path(BASE_DIR).resolve().parent/'config/settings/data/'
            'bagneux.geojson'
        )
        collectivity = self.__create_collectivity(blr_layer)
        collectivity.save(strict=True, verbose=False)
        collectivity = self.__create_collectivity(bag_layer)
        collectivity.save(strict=True, verbose=False)

    def __create_collectivity(self, layer):
        collectivity_mapping = {
            'name': 'nom',
            'insee_code': 'insee',
            'activity': 'activity',
            'feat_geom': 'Polygon',
        }
        collectivities = LayerMapping(
            Collectivity,
            layer,
            collectivity_mapping,
            transform=False
        )
        return collectivities
    
    def emulate_set_collectivity_postal_code(self):
        for collectivity in Collectivity.objects.all():
            for postal_code in PostalCode.objects.all():
                if collectivity.insee_code == postal_code.insee_code:
                    collectivity.postal_code_id = postal_code.id
                    collectivity.save()
