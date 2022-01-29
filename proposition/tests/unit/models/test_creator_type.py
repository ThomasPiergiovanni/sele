"""Test creator type module.
"""
from django.db import models
from django.test import TestCase

from proposition.models.creator_type import CreatorType


class CreatorTypeTest(TestCase):
    """Test CreatorType class.
    """
    def setUp(self):
        self.emulate_creator_type()

    def emulate_creator_type(self):
        """
        """
        CreatorType.objects.create(id=1, name="Collective")
        CreatorType.objects.create(id=2, name="Individuelle")

    def test_status_with_status_class(self):
        creator_type = CreatorType.objects.get(pk=1)
        self.assertIsInstance(creator_type, CreatorType)

    def test_status_with_status_attr_name_characteristic(self):
        attribute = CreatorType._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 16)
        self.assertEqual(attribute.unique, True)
    
    def test_status_with_emulated_status_instance(self):
        creator_type = CreatorType.objects.get(pk=1)
        self.assertEqual(creator_type.name, "Collective")
        creator_type = CreatorType.objects.get(pk=2)
        self.assertEqual(creator_type.name, "Individuelle")


