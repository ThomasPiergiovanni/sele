"""Test category module.
"""
from django.db import models
from django.test import TestCase

from proposition.management.commands.reset_proposition import Command
from proposition.models.category import Category
from proposition.models.kind import Kind


class ResetPropositiionTest(TestCase):
    """Test Reset proposition class.
    """
    def setUp(self):
        """Method that set up data for the entire class
        """
        self.command = Command()

    def test_drop_kind_with_instance_is_none(self):
        Kind.objects.create(id=1, name="Demande")
        Kind.objects.create(id=2, name="Offre")
        kinds = Kind.objects.all()
        self.__check_instance_is_not_none(kinds)
        self.command._Command__drop_kind()
        kinds = Kind.objects.all()
        self.__check_instance_is_none(kinds)
    
    def __check_instance_is_not_none(self, instances):
        for instance in instances:
            self.assertIsNotNone(instance)

    def __check_instance_is_none(self, instances):
        for instance in instances:
            self.assertIsNone(instance)

    def test_insert_kind_with_instances_is_not_none(self):
        kinds = Kind.objects.all()
        self.__check_instance_is_none(kinds)
        self.command._Command__insert_kind()
        kinds = Kind.objects.all()
        self.__check_instance_is_not_none(kinds)


    def test_drop_category_with_instance_is_none(self):
        Category.objects.create(id=1, name="Activité")
        Category.objects.create(id=2, name="Produit")
        categories = Category.objects.all()
        self.__check_instance_is_not_none(categories)
        self.command._Command__drop_category()
        categories = Category.objects.all()
        self.__check_instance_is_none(categories)

    def test_insert_category_with_instances_is_not_none(self):
        categories = Category.objects.all()
        self.__check_instance_is_none(categories)
        self.command._Command__insert_category()
        categories = Category.objects.all()
        self.__check_instance_is_not_none(categories)
