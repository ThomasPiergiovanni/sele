"""Test category module.
"""
from django.db import models
from django.test import TestCase

from proposition.management.commands.reset_proposition import Command
from proposition.models.category import Category
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.rating import Rating
from proposition.models.status import Status


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
    
    def test_drop_domain_with_instance_is_none(self):
        Domain.objects.create(id=1, name="Santé")
        Domain.objects.create(id=2, name="Support à l'entreprise")
        domains = Domain.objects.all()
        self.__check_instance_is_not_none(domains)
        self.command._Command__drop_domain()
        domains = Domain.objects.all()
        self.__check_instance_is_none(domains)

    def test_insert_domain_with_instances_is_not_none(self):
        domains = Domain.objects.all()
        self.__check_instance_is_none(domains)
        self.command._Command__insert_domain()
        domains = Domain.objects.all()
        self.__check_instance_is_not_none(domains)

    def test_drop_status_with_instance_is_none(self):
        Status.objects.create(id=1, name="Annulé")
        Status.objects.create(id=2, name="En cours")
        statuses = Status.objects.all()
        self.__check_instance_is_not_none(statuses)
        self.command._Command__drop_status()
        statuses = Status.objects.all()
        self.__check_instance_is_none(statuses)

    def test_insert_status_with_instances_is_not_none(self):
        statuses = Status.objects.all()
        self.__check_instance_is_none(statuses)
        self.command._Command__insert_status()
        statuses = Status.objects.all()
        self.__check_instance_is_not_none(statuses)

    def test_drop_rating_with_instance_is_none(self):
        Rating.objects.create(id=1, rate=1)
        Rating.objects.create(id=2, rate=2)
        ratings = Rating.objects.all()
        self.__check_instance_is_not_none(ratings)
        self.command._Command__drop_rating()
        ratings = Rating.objects.all()
        self.__check_instance_is_none(ratings)

    def test_insert_ratings_with_instances_is_not_none(self):
        ratings = Rating.objects.all()
        self.__check_instance_is_none(ratings)
        self.command._Command__insert_rating()
        ratings = Rating.objects.all()
        self.__check_instance_is_not_none(ratings)
