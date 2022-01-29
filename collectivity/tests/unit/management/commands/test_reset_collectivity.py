"""Test collectivity reset module.
"""
from django.contrib.gis.utils import LayerMapping
from django.test import TestCase
from pathlib import Path

from collectivity.management.commands.reset_collectivity import Command
from collectivity.models.collectivity import Collectivity
from collectivity.models.postal_code import PostalCode
from collectivity.tests.unit.models.test_collectivity import CollectivityTest
from collectivity.tests.unit.models.test_postal_code import PostalCodeTest
from config.settings import BASE_DIR


class ResetCollectivityTest(TestCase):
    """Test Reset collectivity class.
    """
    def setUp(self):
        """Method that set up data for the entire class
        """
        self.command = Command()

    def test_drop_collectivity_with_instance_is_none(self):
        CollectivityTest().emulate_collectivity()
        collectivities = Collectivity.objects.all()
        self.assertTrue(collectivities)
        self.command._Command__drop_collectivity()
        collectivities = Collectivity.objects.all()
        self.assertFalse(collectivities)

    def test_insert_collectivities_with_instances_is_not_none(self):
        collectivities = Collectivity.objects.all()
        self.assertFalse(collectivities)
        self.command._Command__insert_collectivity()
        collectivities = Collectivity.objects.all()
        self.assertTrue(collectivities)

    def test_drop_postal_code_with_instance_is_none(self):
        PostalCodeTest().emulate_postal_code()
        postal_codes = PostalCode.objects.all()
        self.assertTrue(postal_codes)
        self.command._Command__drop_postal_code()
        postal_codes = PostalCode.objects.all()
        self.assertFalse(postal_codes)

    def test_insert_postal_code_with_instances_is_not_none(self):
        CollectivityTest().emulate_collectivity()
        postal_codes = PostalCode.objects.all()
        self.assertFalse(postal_codes)
        self.command._Command__insert_postal_code()
        postal_codes = PostalCode.objects.all()
        self.assertTrue(postal_codes)

