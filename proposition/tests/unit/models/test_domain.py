# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.db import models
from django.test import TestCase

from proposition.models.domain import Domain
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class DomainTest(TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_domain_with_class(self):
        self.proposition_emulation.emulate_domain()
        instance = Domain.objects.get(pk=1)
        self.assertIsInstance(instance, Domain)

    def test_domain_with_attr_name_characteristic(self):
        self.proposition_emulation.emulate_domain()
        attribute = Domain._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 128)
        self.assertEqual(attribute.unique, True)

    def test_domain_with_emulated_instance(self):
        self.proposition_emulation.emulate_domain()
        instance = Domain.objects.get(pk=1)
        self.assertEqual(instance.name, "Santé")
        instance = Domain.objects.get(pk=2)
        self.assertEqual(instance.name, "Support à l'entreprise")
