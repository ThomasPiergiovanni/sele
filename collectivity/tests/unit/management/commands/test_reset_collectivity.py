# pylint: disable=C0114,C0115,C0116,E1101,R0201,W0212
from django.test import TestCase

from collectivity.management.commands.reset_collectivity import Command
from collectivity.models.collectivity import Collectivity
from collectivity.models.postal_code import PostalCode
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)


class ResetCollectivityTest(TestCase):
    def setUp(self):
        self.command = Command()
        self.command.testing = True
        self.collectivity_emulation = CollectivityEmulation()

    def test_drop_postal_code_with_instance_is_none(self):
        self.collectivity_emulation.emulate_postal_code()
        postal_codes = PostalCode.objects.all()
        self.assertTrue(postal_codes)
        self.command._Command__drop_postal_code()
        postal_codes = PostalCode.objects.all()
        self.assertFalse(postal_codes)

    def test_insert_postal_code_with_instances_is_not_none(self):
        postal_codes = PostalCode.objects.all()
        self.assertFalse(postal_codes)
        self.command._Command__insert_postal_code()
        postal_codes = PostalCode.objects.all()
        self.assertTrue(postal_codes)

    def test_drop_collectivity_with_instance_is_none(self):
        self.collectivity_emulation.emulate_collectivity()
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

    def test___set_collectivity_postal_code_with_instances_is_not_none(self):
        self.collectivity_emulation.emulate_postal_code()
        self.collectivity_emulation.emulate_collectivity()
        collectivity = Collectivity.objects.all().last()
        self.assertFalse(collectivity.postal_code)
        self.command._Command__set_collectivity_postal_code()
        collectivity = Collectivity.objects.all().last()
        self.assertTrue(collectivity.postal_code)
