"""Test category module.
"""
from django.db import models
from django.test import TestCase

from proposition.models.kind import Kind


class KindTest(TestCase):
    """Test kind class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_kind()

    @classmethod
    def emulate_kind(cls):
        Kind.objects.create(id=1, name="Demande")
        Kind.objects.create(id=2, name="Offre")

    def test_kind_with_kind_class(self):
        kind = Kind.objects.get(pk=1)
        self.assertIsInstance(kind, Kind)

    def test_kind_with_kind_attr_name_characteristic(self):
        kind_attribute = Kind._meta.get_field('name')
        self.assertTrue(kind_attribute)
        self.assertEqual(type(kind_attribute),type(models.CharField()))
        self.assertEqual(kind_attribute.max_length, 32)
        self.assertEqual(kind_attribute.unique, True)
    
    def test_kind_with_emulated_kind_instance(self):
        kind = Kind.objects.get(pk=1)
        self.assertEqual(kind.name, "Demande")
        kind = Kind.objects.get(pk=2)
        self.assertEqual(kind.name, "Offre")


