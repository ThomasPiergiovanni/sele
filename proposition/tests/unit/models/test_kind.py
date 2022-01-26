"""Test category module.
"""
from django.db import models
from django.test import TestCase

from proposition.models.kind import Kind


class KindTest(TestCase):
    """Test kind class.
    """
    def setUp(self):
        self.emulate_kind()

    def emulate_kind(self):
        """
        """
        Kind.objects.create(id=1, name="Demande")
        Kind.objects.create(id=2, name="Offre")

    def test_kind_with_kind_class(self):
        kind = Kind.objects.get(pk=1)
        self.assertIsInstance(kind, Kind)

    def test_kind_with_kind_attr_name_characteristic(self):
        attribute = Kind._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 32)
        self.assertEqual(attribute.unique, True)
    
    def test_kind_with_emulated_kind_instance(self):
        kind = Kind.objects.get(pk=1)
        self.assertEqual(kind.name, "Demande")
        kind = Kind.objects.get(pk=2)
        self.assertEqual(kind.name, "Offre")


