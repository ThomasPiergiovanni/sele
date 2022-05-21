# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.db import models
from django.test import TestCase

from proposition.models.category import Category
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class CategoryTest(TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_category_with_instance(self):
        self.proposition_emulation.emulate_category()
        instance = Category.objects.get(pk=1)
        self.assertTrue(instance, Category)

    def test_category_with_attr_name_characteristic(self):
        self.proposition_emulation.emulate_category()
        attribute = Category._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 32)
        self.assertEqual(attribute.unique, True)

    def test_category_with_emulated_instance(self):
        self.proposition_emulation.emulate_category()
        instance = Category.objects.get(pk=1)
        self.assertEqual(instance.name, "Activité")
        instance = Category.objects.get(pk=2)
        self.assertEqual(instance.name, "Produit")
