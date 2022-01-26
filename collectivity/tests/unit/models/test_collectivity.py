"""Test rating module.
"""
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.db import models
from django.test import TestCase
from pathlib import Path

from collectivity.models.collectivity import Collectivity
from config.settings import BASE_DIR

class CollectivityTest(TestCase):
    """Test collectivity class.
    """

    def setUp(self):
        self.emulate_collectivity()

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
        collectivity = self._create_collectivity(blr_layer)
        collectivity.save(strict=True, verbose=False)
        collectivity = self._create_collectivity(bag_layer)
        collectivity.save(strict=True, verbose=False)

    def _create_collectivity(self, layer):
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

    def test_collectivity_with_collectivity_class(self):
        collectivity = Collectivity.objects.last()
        self.assertIsInstance(collectivity, Collectivity)

    def test_collectivity_with_attr_name_characteristic(self):
        attribute = Collectivity._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 256)
        self.assertEqual(attribute.unique, False)

    def test_collectivity_with_attr_insee_code_characteristic(self):
        attribute = Collectivity._meta.get_field('insee_code')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 5)
        self.assertEqual(attribute.unique, False)

    def test_collectivity_with_activity_code_characteristic(self):
        attribute = Collectivity._meta.get_field('activity')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 3)
        self.assertEqual(attribute.unique, False)

    def test_collectivity_with_feat_geom_code_characteristic(self):
        attribute = Collectivity._meta.get_field('feat_geom')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.MultiPolygonField()))

    
    def test_status_with_emulated_status_instance(self):
        collectivity = Collectivity.objects.order_by('-id')[:2][0]
        self.assertEqual(collectivity.name, "Bagneux")
        collectivity = Collectivity.objects.order_by('-id')[:2][1]
        self.assertEqual(collectivity.name, "Bourg-la-Reine")
