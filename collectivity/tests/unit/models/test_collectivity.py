# pylint: disable=C0114,C0115,C0116,E1101,R0201,W0212
from django.contrib.gis.db import models
from django.test import TestCase

from collectivity.models.collectivity import Collectivity
from collectivity.models.postal_code import PostalCode
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)


class CollectivityTest(TestCase):

    def setUp(self):
        self.collectivity_emulation = CollectivityEmulation()
        self.collectivity_emulation.emulate_collectivity()

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

    def test_postal_code_with_attr_insee_code_characteristic(self):
        attribute = Collectivity._meta.get_field('postal_code')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(PostalCode, on_delete=models.CASCADE))
        )

    def test_status_with_emulated_status_instance(self):
        self.collectivity_emulation.emulate_postal_code()
        self.collectivity_emulation.emulate_collectivity()
        self.collectivity_emulation.emulate_set_collectivity_postal_code()
        collectivity = Collectivity.objects.order_by('-id')[:2][0]
        self.assertEqual(collectivity.name, 'Bagneux')
        self.assertEqual(collectivity.postal_code.postal_code, '92220')
        collectivity = Collectivity.objects.order_by('-id')[:2][1]
        self.assertEqual(collectivity.name, 'Bourg-la-Reine')
        self.assertEqual(collectivity.postal_code.postal_code, '92340')
