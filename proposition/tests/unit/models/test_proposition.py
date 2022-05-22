# pylint: disable=C0114,C0115,C0116,E1101,W0106,W0212
from datetime import date, datetime

from django.db import models , utils
from django.test import TestCase
from django.utils import timezone

from authentication.models import CustomUser
from chat.models import Discussion
from proposition.models import (
    Category, CreatorType, Domain, Kind, Proposition, Rating, Status
)
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class PropositionTest(TestCase):
    """Test Proposition class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_test_setup()

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
        self.assertEqual(type(attribute), type(models.PositiveIntegerField()))
        self.assertEqual(attribute.null, False)
        self.assertEqual(attribute.default, 60)
        self.assertEqual(attribute.validators[0].limit_value, 1)

    def test_proposition_with_attr_category_characteristic(self):
        attribute = Proposition._meta.get_field('proposition_category')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ForeignKey(
                    Category,
                    on_delete=models.CASCADE,
                    related_name='proposition_category'
                )
            )
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_creator_characteristic(self):
        attribute = Proposition._meta.get_field('proposition_creator')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ForeignKey(
                    CustomUser,
                    on_delete=models.CASCADE,
                    related_name='proposition_creator'
                )
            )
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_creator_type_characteristic(self):
        attribute = Proposition._meta.get_field('proposition_creator_type')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ForeignKey(
                    CreatorType,
                    on_delete=models.CASCADE,
                    related_name='proposition_creator_type'
                )
            )
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_domain_characteristic(self):
        attribute = Proposition._meta.get_field('proposition_domain')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ForeignKey(
                    Domain,
                    on_delete=models.CASCADE,
                    related_name='proposition_domain'
                )
            )
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_kind_characteristic(self):
        attribute = Proposition._meta.get_field('proposition_kind')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ForeignKey(
                    Kind,
                    on_delete=models.CASCADE,
                    related_name='proposition_kind'
                )
            )
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_rating_characteristic(self):
        attribute = Proposition._meta.get_field('proposition_rating')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ForeignKey(
                    Rating,
                    on_delete=models.CASCADE,
                    related_name='proposition_rating'
                )
            )
        )
        self.assertEqual(attribute.null, True)

    def test_proposition_with_attr_status_characteristic(self):
        attribute = Proposition._meta.get_field('proposition_status')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ForeignKey(
                    Status,
                    on_delete=models.CASCADE,
                    related_name='proposition_status'
                )
            )
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_attr_taker_characteristic(self):
        attribute = Proposition._meta.get_field('proposition_taker')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ForeignKey(
                    CustomUser,
                    on_delete=models.CASCADE,
                    related_name='proposition_taker'
                )
            )
        )
        self.assertEqual(attribute.null, True)

    def test_proposition_with_attr_proposition_discussion(self):
        attribute = Proposition._meta.get_field('proposition_discussion')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(
                models.ForeignKey(
                    Discussion,
                    on_delete=models.CASCADE,
                    related_name='proposition_taker'
                )
            )
        )
        self.assertEqual(attribute.null, False)

    def test_proposition_with_emulated_question_instance(self):
        proposition = Proposition.objects.get(pk=1)
        self.assertEqual(proposition.name, "DCours1")
        self.assertEqual(
            proposition.creation_date,
            datetime(2022, 1, 1, 21, 56, 22, tzinfo=timezone.utc)
        )
        self.assertEqual(
            proposition.proposition_creator.email, "user1@email.com"
        )
        self.assertEqual(
            proposition.proposition_taker.email, "user3@email.com"
        )
        self.assertEqual(
            proposition.proposition_creator_type.name, "Collective"
        )
        self.assertEqual(proposition.proposition_status.name, "Annulé")
        self.assertEqual(
            proposition.proposition_discussion.subject, "Sujet est HTML"
        )
        proposition = Proposition.objects.get(pk=2)
        self.assertEqual(proposition.name, "DCours2")
        self.assertEqual(proposition.start_date, date(2022, 1, 1))
        self.assertEqual(
            proposition.proposition_creator_type.name, "Collective"
        )

    def test_proposition_with_wrong_dates(self):
        Proposition.objects.all().delete()
        proposition = True
        try:
            Proposition.objects.create(
                id=100,
                name="Cours de Python",
                description=(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                    " amet, adipiscing nec, ultricies sed, dolor. Cras elem-"
                    " entum ultrices diam. Maecenas ligula massa, varius a"
                ),
                creation_date=datetime(
                    2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
                ),
                start_date=date(2022, 2, 25),
                end_date=date(2022, 1, 25),
                duration=120,
                proposition_category_id=2,
                proposition_creator_id=1,
                proposition_creator_type_id=1,
                proposition_domain_id=1,
                proposition_kind_id=1,
                proposition_rating_id=1,
                proposition_status_id=1,
                proposition_taker_id=2,
                proposition_discussion_id=1
            )
            proposition = Proposition.objects.get(pk=100)
        except utils.IntegrityError:
            proposition = False
        self.assertFalse(proposition)

    def test_proposition_with_samecreator_taker(self):
        Proposition.objects.all().delete()
        proposition = True
        try:
            Proposition.objects.create(
                id=101,
                name="Cours de Python",
                description=(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                    " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                    " amet, adipiscing nec, ultricies sed, dolor. Cras elemen-"
                    " tum ultrices diam. Maecenas ligula massa, varius a"
                ),
                creation_date=datetime(
                    2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
                ),
                start_date=date(2022, 2, 25),
                end_date=date(2022, 3, 25),
                duration=120,
                proposition_category_id=2,
                proposition_creator_id=1,
                proposition_creator_type_id=1,
                proposition_domain_id=1,
                proposition_kind_id=1,
                proposition_rating_id=1,
                proposition_status_id=1,
                proposition_taker_id=1,
                proposition_discussion_id=1
            )
            proposition = Proposition.objects.get(pk=101)
        except utils.IntegrityError:
            proposition = False
        self.assertFalse(proposition)
