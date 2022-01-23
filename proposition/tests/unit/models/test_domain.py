"""Test category module.
"""
from django.db import models
from django.test import TestCase

from proposition.models.domain import Domain


class DomainTest(TestCase):
    """Test domain class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_domain()

    @classmethod
    def emulate_domain(cls):
        Domain.objects.create(id=1, name="Santé")
        Domain.objects.create(id=2, name="Support à l'entreprise")

    def test_domain_with_class(self):
        instance = Domain.objects.get(pk=1)
        self.assertIsInstance(instance, Domain)

    def test_domain_with_attr_name_characteristic(self):
        attribute = Domain._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 128)
        self.assertEqual(attribute.unique, True)
    
    def test_domain_with_emulated_instance(self):
        instance = Domain.objects.get(pk=1)
        self.assertEqual(instance.name, "Santé")
        instance = Domain.objects.get(pk=2)
        self.assertEqual(instance.name, "Support à l'entreprise")


