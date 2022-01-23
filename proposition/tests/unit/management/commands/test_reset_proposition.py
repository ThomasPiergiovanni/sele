"""Test category module.
"""
from django.db import models
from django.test import TestCase

from proposition.management.commands.reset_proposition import Command
from proposition.models.kind import Kind


class ResetPropositiionTest(TestCase):
    """Test Reset proposition class.
    """
    def setUp(self):
        """Method that set up data for the entire class
        """
        self.command = Command()

    def test_drop_kind_with_object_is_none(self):
        Kind.objects.create(id=1, name="Demande")
        Kind.objects.create(id=2, name="Offre")
        kinds = Kind.objects.all()
        for kind in kinds:
            self.assertIsNotNone(kind)
        self.command._Command__drop_kind()
        kinds = Kind.objects.all()
        for kind in kinds:
            self.assertIsNone(kind)

    def test_insert_kind_with_objects_is_not_none(self):
        kinds = Kind.objects.all()
        for kind in kinds:
            self.assertIsNone(kind)
        self.command._Command__insert_kind()
        kinds = Kind.objects.all()
        for kind in kinds:
            self.assertIsNotNone(kind)
