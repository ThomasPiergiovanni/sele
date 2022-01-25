"""Test collectivity reset module.
"""
from django.contrib.gis.utils import LayerMapping
from django.test import TestCase
from pathlib import Path

from collectivity.management.commands.reset_collectivity import Command
from collectivity.models.collectivity import Collectivity
from config.settings import BASE_DIR


class ResetCollectivityTest(TestCase):
    """Test Reset collectivity class.
    """
    def setUp(self):
        """Method that set up data for the entire class
        """
        self.command = Command()

    def test_drop_kind_with_instance_is_none(self):
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
        collectivity = LayerMapping(
            Collectivity,
            blr_layer,
            collectivity_mapping,
            transform=False
        )
        collectivity.save(strict=True, verbose=True)
        collectivity = LayerMapping(
            Collectivity,
            bag_layer,
            collectivity_mapping,
            transform=False
        )
        collectivity.save(strict=True, verbose=True)
        collectivities = Collectivity.objects.all()
        self.__check_instance_is_not_none(collectivities)
        self.command._Command__drop_collectivity()
        collectivities = Collectivity.objects.all()
        self.__check_instance_is_none(collectivities)
    
    def __check_instance_is_not_none(self, instances):
        for instance in instances:
            self.assertIsNotNone(instance)

    def __check_instance_is_none(self, instances):
        for instance in instances:
            self.assertIsNone(instance)

    def test_insert_collectivities_with_instances_is_not_none(self):
        collectivities = Collectivity.objects.all()
        self.__check_instance_is_none(collectivities)
        self.command._Command__insert_collectivity()
        collectivities = Collectivity.objects.all()
        self.__check_instance_is_not_none(collectivities)
