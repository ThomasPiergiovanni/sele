"""Test rating module.
"""
from django.db import models
from django.test import TestCase

from proposition.models.rating import Rating


class RatingTest(TestCase):
    """Test rating class.
    """
    def setUp(self):
        self.emulate_rating()

    def emulate_rating(self):
        """
        """
        Rating.objects.create(id=1, rate=1)
        Rating.objects.create(id=2, rate=2)

    def test_status_with_status_class(self):
        rating = Rating.objects.get(pk=1)
        self.assertIsInstance(rating, Rating)

    def test_status_with_status_attr_name_characteristic(self):
        attribute = Rating._meta.get_field('rate')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.IntegerField()))
        self.assertEqual(attribute.validators[0].limit_value, 1)
        self.assertEqual(attribute.validators[1].limit_value, 5)
    
    def test_status_with_emulated_status_instance(self):
        rating = Rating.objects.get(pk=1)
        self.assertEqual(rating.rate, 1)
        rating = Rating.objects.get(pk=2)
        self.assertEqual(rating.rate, 2)


