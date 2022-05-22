# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.db import models
from django.test import TestCase

from proposition.models import Kind
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class KindTest(TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_kind_with_kind_class(self):
        self.proposition_emulation.emulate_kind()
        kind = Kind.objects.get(pk=1)
        self.assertIsInstance(kind, Kind)

    def test_kind_with_kind_attr_name_characteristic(self):
        self.proposition_emulation.emulate_kind()
        attribute = Kind._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 32)
        self.assertEqual(attribute.unique, True)

    def test_kind_with_emulated_kind_instance(self):
        self.proposition_emulation.emulate_kind()
        kind = Kind.objects.get(pk=1)
        self.assertEqual(kind.name, "Demande")
        kind = Kind.objects.get(pk=2)
        self.assertEqual(kind.name, "Offre")
