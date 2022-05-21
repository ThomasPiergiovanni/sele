# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.db import models
from django.test import TestCase

from proposition.models.rating import Rating
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class RatingTest(TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_status_with_status_class(self):
        self.proposition_emulation.emulate_rating()
        rating = Rating.objects.get(pk=1)
        self.assertIsInstance(rating, Rating)

    def test_status_with_status_attr_name_characteristic(self):
        self.proposition_emulation.emulate_rating()
        attribute = Rating._meta.get_field('rate')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.IntegerField()))
        self.assertEqual(attribute.validators[0].limit_value, 1)
        self.assertEqual(attribute.validators[1].limit_value, 5)

    def test_status_with_emulated_status_instance(self):
        self.proposition_emulation.emulate_rating()
        rating = Rating.objects.get(pk=1)
        self.assertEqual(rating.rate, 1)
        rating = Rating.objects.get(pk=2)
        self.assertEqual(rating.rate, 2)
