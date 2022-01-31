"""Test proposition method module.
"""
from datetime import date, datetime

from django.db import models
from django.test import TestCase
from django.utils import timezone

from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from proposition.models.category import Category
from proposition.models.creator_type import CreatorType
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.proposition import Proposition
from proposition.models.rating import Rating
from proposition.models.status import Status
from proposition.tests.unit.models.test_category import CategoryTest
from proposition.tests.unit.models.test_creator_type import CreatorTypeTest
from proposition.tests.unit.models.test_domain import DomainTest
from proposition.tests.unit.models.test_kind import KindTest
from proposition.tests.unit.models.test_rating import RatingTest
from proposition.tests.unit.models.test_status import StatusTest



class PropositionTest(TestCase):
    """Test Proposition class.
    """
    def setUp(self):
        self.emulate_proposition()

    def emulate_proposition(self):
        """
        """
        CustomUserTest().emulate_custom_user()
        CategoryTest().emulate_category()
        CreatorTypeTest().emulate_creator_type()
        DomainTest().emulate_domain()
        KindTest().emulate_kind()
        RatingTest().emulate_rating()
        StatusTest().emulate_status()
        # timezone.now()
        Proposition.objects.create(
            id=1,
            name="Cours de Python",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
            ),
            creation_date=datetime(
                2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2021, 12, 25),
            end_date=date(2022, 1, 25),
            duration=120,
            category_id=2,
            creator_id=1,
            creator_type_id=1,
            domain_id=1,
            kind_id=1,
            rating_id=1,
            status_id=1,
            taker_id=2
        ),
        Proposition.objects.create(
            id=2,
            name="Nettoyage du Mur",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
            ),
            creation_date=datetime(
                2022, 1, 23, 8, 21, 3, tzinfo=timezone.utc
            ),
            start_date=date(2021, 12, 28),
            end_date=date(2022, 1, 3),
            duration=3680,
            category_id=2,
            creator_id=2,
            creator_type_id=2,
            domain_id=2,
            kind_id=2,
            rating_id=2,
            status_id=2,
            taker_id=1
        )

    def test_propositon_with_discussion_class(self):
        proposition = Proposition.objects.get(pk=1)
        self.assertIsInstance(proposition, Proposition)

    def test_proposition_with_attr_subject_characteristic(self):
        attribute = Proposition._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 128)
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_description_characteristic(self):
        attribute = Proposition._meta.get_field('description')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.TextField()))
        self.assertEqual(attribute.max_length, 1000)
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_creation_date_characteristic(self):
        attribute = Proposition._meta.get_field('creation_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateTimeField()))
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_start_date_characteristic(self):
        attribute = Proposition._meta.get_field('start_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateField()))
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_end_date_characteristic(self):
        attribute = Proposition._meta.get_field('end_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateField()))
        self.assertEqual(attribute.null, False)

    def test_proposition_user_with_attr_duration_characteristic(self):
        attribute = Proposition._meta.get_field('duration')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.IntegerField()))
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_category_characteristic(self):
        attribute = Proposition._meta.get_field('category')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Category, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_creator_characteristic(self):
        attribute = Proposition._meta.get_field('creator')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_creator_type_characteristic(self):
        attribute = Proposition._meta.get_field('creator_type')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CreatorType, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_domain_characteristic(self):
        attribute = Proposition._meta.get_field('domain')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Domain, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_kind_characteristic(self):
        attribute = Proposition._meta.get_field('kind')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Kind, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_rating_characteristic(self):
        attribute = Proposition._meta.get_field('rating')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Rating, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_status_characteristic(self):
        attribute = Proposition._meta.get_field('status')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Status, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_taker_characteristic(self):
        attribute = Proposition._meta.get_field('taker')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, True)
    
    def test_proposition_with_emulated_question_instance(self):
        proposition = Proposition.objects.get(pk=1)
        self.assertEqual(proposition.name, "Cours de Python")
        self.assertEqual(
            proposition.creation_date,
            datetime(2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc)
        )
        self.assertEqual(proposition.creator.email, "user1@email.com")
        self.assertEqual(proposition.taker.email, "user2@email.com")
        self.assertEqual(proposition.creator_type.name, "Collective")
        self.assertEqual(proposition.status.name, "Annulé")
        proposition = Proposition.objects.get(pk=2)
        self.assertEqual(proposition.name, "Nettoyage du Mur")
        self.assertEqual(proposition.start_date, date(2021, 12, 28))
        self.assertEqual(proposition.creator_type.name, "Individuelle")

