"""Test status module.
"""
from django.db import models
from django.test import TestCase

from proposition.models.status import Status
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)

class StatusTest(TestCase):
    """Test status class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_status_with_status_class(self):
        self.proposition_emulation.emulate_status()
        status = Status.objects.get(pk=1)
        self.assertIsInstance(status, Status)

    def test_status_with_status_attr_name_characteristic(self):
        self.proposition_emulation.emulate_status()
        attribute = Status._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 16)
        self.assertEqual(attribute.unique, True)
    
    def test_status_with_emulated_status_instance(self):
        self.proposition_emulation.emulate_status()
        status = Status.objects.get(pk=1)
        self.assertEqual(status.name, "Annulé")
        status = Status.objects.get(pk=2)
        self.assertEqual(status.name, "En cours")


