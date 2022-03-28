"""Test proposition method module.
"""
from datetime import date, datetime

from django.db import models
from django.test import TestCase
from django.utils import timezone

from authentication.models import CustomUser
from proposition.models.blocked_taker import BlockedTaker
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



class PropositionTest(TestCase):
    """Test Proposition class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_propositon_with_discussion_class(self):
        self.proposition_emulation.emulate_proposition()
        proposition = Proposition.objects.get(pk=1)
        self.assertIsInstance(proposition, Proposition)

    def test_proposition_with_attr_subject_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 128)
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_description_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('description')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.TextField()))
        self.assertEqual(attribute.max_length, 1000)
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_creation_date_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('creation_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateTimeField()))
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_start_date_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('start_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateField()))
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_end_date_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('end_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateField()))
        self.assertEqual(attribute.null, False)

    def test_proposition_user_with_attr_duration_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('duration')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.IntegerField()))
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_category_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('proposition_category')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Category, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_creator_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('proposition_creator')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_creator_type_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('proposition_creator_type')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CreatorType, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_domain_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('proposition_domain')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Domain, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_kind_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('proposition_kind')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Kind, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_rating_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('proposition_rating')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Rating, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_status_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('proposition_status')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Status, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_taker_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('proposition_taker')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, True)

    def test_proposition_with_attr_realtion_custom_user_characteristic(self):
        self.proposition_emulation.emulate_proposition()
        attribute = Proposition._meta.get_field('blocked_takers')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ManyToManyField(
                    CustomUser,
                    models.CASCADE,
                    through='BlockedTaker'
                )
            )
        )
    
    def test_proposition_with_emulated_question_instance(self):
        self.proposition_emulation.emulate_proposition()
        proposition = Proposition.objects.get(pk=1)
        self.assertEqual(proposition.name, "Cours de Python")
        self.assertEqual(
            proposition.creation_date,
            datetime(2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc)
        )
        self.assertEqual(
            proposition.proposition_creator.email, "user1@email.com"
        )
        self.assertEqual(
            proposition.proposition_taker.email, "user2@email.com"
        )
        self.assertEqual(
            proposition.proposition_creator_type.name, "Collective"
        )
        self.assertEqual(proposition.proposition_status.name, "Annulé")
        proposition = Proposition.objects.get(pk=2)
        self.assertEqual(proposition.name, "Nettoyage du Mur")
        self.assertEqual(proposition.start_date, date(2021, 12, 28))
        self.assertEqual(
            proposition.proposition_creator_type.name, "Individuelle"
        )

