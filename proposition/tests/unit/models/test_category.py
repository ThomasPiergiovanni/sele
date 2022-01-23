"""Test category module.
"""
from django.db import models
from django.test import TestCase

from proposition.models.category import Category


class CategoryTest(TestCase):
    """Test category class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_category()

    @classmethod
    def emulate_category(cls):
        """
        """
        Category.objects.create(id=1, name="Activité")
        Category.objects.create(id=2, name="Produit")

    def test_category_with_class(self):
        instance = Category.objects.get(pk=1)
        self.assertIsInstance(instance, Category)

    def test_category_with_attr_name_characteristic(self):
        attribute = Category._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 32)
        self.assertEqual(attribute.unique, True)
    
    def test_category_with_emulated_instance(self):
        instance = Category.objects.get(pk=1)
        self.assertEqual(instance.name, "Activité")
        instance = Category.objects.get(pk=2)
        self.assertEqual(instance.name, "Produit")


