# pylint: disable=C0114,C0115,C0116,E1101,R0801,W0212
from django.db import models
from django.test import TestCase

from proposition.models.creator_type import CreatorType
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class CreatorTypeTest(TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_status_with_status_class(self):
        self.proposition_emulation.emulate_creator_type()
        creator_type = CreatorType.objects.get(pk=1)
        self.assertIsInstance(creator_type, CreatorType)

    def test_status_with_status_attr_name_characteristic(self):
        self.proposition_emulation.emulate_creator_type()
        attribute = CreatorType._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 16)
        self.assertEqual(attribute.unique, True)

    def test_status_with_emulated_status_instance(self):
        self.proposition_emulation.emulate_creator_type()
        creator_type = CreatorType.objects.get(pk=1)
        self.assertEqual(creator_type.name, "Collective")
        creator_type = CreatorType.objects.get(pk=2)
        self.assertEqual(creator_type.name, "Individuelle")
