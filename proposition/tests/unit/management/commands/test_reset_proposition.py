"""Test category module.
"""
from django.db import models
from django.test import TestCase

from proposition.management.commands.reset_proposition import Command
from proposition.models.category import Category
from proposition.models.creator_type import CreatorType
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.proposition import Proposition
from proposition.models.rating import Rating
from proposition.models.status import Status
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class ResetPropositiionTest(TestCase):
    """Test Reset proposition class.
    """
    def setUp(self):
        """Method that set up data for the entire class
        """
        self.command = Command()
        self.proposition_emulation = PropositionEmulation()

    def test_drop_kind_with_instance_is_none(self):
        self.proposition_emulation.emulate_kind()
        kinds = Kind.objects.all()
        self.assertTrue(kinds)
        self.command._Command__drop_kind()
        kinds = Kind.objects.all()
        self.assertFalse(kinds)

    def test_insert_kind_with_instances_is_not_none(self):
        kinds = Kind.objects.all()
        self.assertFalse(kinds)
        self.command._Command__insert_kind()
        kinds = Kind.objects.all()
        self.assertTrue(kinds)

    def test_drop_category_with_instance_is_none(self):
        self.proposition_emulation.emulate_category()
        categories = Category.objects.all()
        self.assertTrue(categories)
        self.command._Command__drop_category()
        categories = Category.objects.all()
        self.assertFalse(categories)

    def test_insert_category_with_instances_is_not_none(self):
        categories = Category.objects.all()
        self.assertFalse(categories)
        self.command._Command__insert_category()
        categories = Category.objects.all()
        self.assertTrue(categories)


    def test_drop_creator_type_with_instance_is_none(self):
        self.proposition_emulation.emulate_creator_type()
        creator_types = CreatorType.objects.all()
        self.assertTrue(creator_types)
        self.command._Command__drop_creator_type()
        creator_types = CreatorType.objects.all()
        self.assertFalse(creator_types)

    def test_insert_creator_type_with_instances_is_not_none(self):
        creator_types = CreatorType.objects.all()
        self.assertFalse(creator_types)
        self.command._Command__insert_creator_type()
        creator_types = CreatorType.objects.all()
        self.assertTrue(creator_types)
    
    def test_drop_domain_with_instance_is_none(self):
        self.proposition_emulation.emulate_domain()
        domains = Domain.objects.all()
        self.assertTrue(domains)
        self.command._Command__drop_domain()
        domains = Domain.objects.all()
        self.assertFalse(domains)

    def test_insert_domain_with_instances_is_not_none(self):
        domains = Domain.objects.all()
        self.assertFalse(domains)
        self.command._Command__insert_domain()
        domains = Domain.objects.all()
        self.assertTrue(domains)

    def test_drop_rating_with_instance_is_none(self):
        self.proposition_emulation.emulate_rating()
        ratings = Rating.objects.all()
        self.assertTrue(ratings)
        self.command._Command__drop_rating()
        ratings = Rating.objects.all()
        self.assertFalse(ratings)

    def test_insert_ratings_with_instances_is_not_none(self):
        ratings = Rating.objects.all()
        self.assertFalse(ratings)
        self.command._Command__insert_rating()
        ratings = Rating.objects.all()
        self.assertTrue(ratings)

    def test_drop_status_with_instance_is_none(self):
        self.proposition_emulation.emulate_status()
        statuses = Status.objects.all()
        self.assertTrue(statuses)
        self.command._Command__drop_status()
        statuses = Status.objects.all()
        self.assertFalse(statuses)

    def test_insert_status_with_instances_is_not_none(self):
        statuses = Status.objects.all()
        self.assertFalse(statuses)
        self.command._Command__insert_status()
        statuses = Status.objects.all()
        self.assertTrue(statuses)

    def test_drop_proposition_with_instance_is_none(self):
        self.proposition_emulation.emulate_proposition()
        propositions = Proposition.objects.all()
        self.assertTrue(propositions)
        self.command._Command__drop_proposition()
        propositions = Proposition.objects.all()
        self.assertFalse(propositions)


