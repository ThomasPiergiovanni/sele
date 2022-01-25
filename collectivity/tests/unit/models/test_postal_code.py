"""Test rating module.
"""

from django.db import models
from django.test import TestCase
from pathlib import Path

from collectivity.models.postal_code import PostalCode


class PostalCodeTest(TestCase):
    """Test postal code class.
    """
    @classmethod
    def setUp(cls):
        cls.emulate_postal_code()

    @classmethod
    def emulate_postal_code(cls):
        """
        """
        PostalCode.objects.create(
            id=1, postal_code='01100', insee_code='01011'
        )
        PostalCode.objects.create(
            id=2, postal_code='01480', insee_code='01021'
        )

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
        self.assertEqual(postal_code.postal_code, "01100")
        postal_code = PostalCode.objects.get(pk=2)
        self.assertEqual(postal_code.postal_code, "01480")
