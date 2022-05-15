# pylint: disable=C0114,C0115,C0116,E1101,R0201,W0212
from django.db import models
from django.test import TestCase

from collectivity.models.postal_code import PostalCode
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)


class PostalCodeTest(TestCase):

    def setUp(self):
        self.collectivity_emulation = CollectivityEmulation()
        self.collectivity_emulation.emulate_postal_code()

    def test_postal_code_with_postal_code_class(self):
        postal_code = PostalCode.objects.last()
        self.assertIsInstance(postal_code, PostalCode)

    def test_postal_code_with_attr_postal_code_characteristic(self):
        attribute = PostalCode._meta.get_field('postal_code')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 5)
        self.assertEqual(attribute.unique, False)

    def test_postal_code_with_attr_insee_code_characteristic(self):
        attribute = PostalCode._meta.get_field('insee_code')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 5)
        self.assertEqual(attribute.unique, False)

    def test_postal_code_with_emulated_postal_code_instance(self):
        postal_code = PostalCode.objects.get(pk=1)
        self.assertEqual(postal_code.postal_code, "92340")
        postal_code = PostalCode.objects.get(pk=2)
        self.assertEqual(postal_code.postal_code, "92220")
