# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.db import models
from django.test import TestCase

from vote.models.voting_method import VotingMethod
from vote.tests.emulation.vote_emulation import VoteEmulation


class VotingMethodTest(TestCase):

    def setUp(self):
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_voting_method()

    def test_voting_methods_with_status_class(self):
        voting_method = VotingMethod.objects.get(pk=1)
        self.assertIsInstance(voting_method, VotingMethod)

    def test_voting_method_with_attr_name_characteristic(self):
        attribute = VotingMethod._meta.get_field('name')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 32)
        self.assertEqual(attribute.unique, True)

    def test_voting_method_with_attr_percentage_characteristic(self):
        attribute = VotingMethod._meta.get_field('percentage')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DecimalField()))
        self.assertEqual(attribute.validators[0].limit_value, 0.01)
        self.assertEqual(attribute.validators[1].limit_value, 1)
        self.assertEqual(attribute.max_digits, 3)
        self.assertEqual(attribute.decimal_places, 2)

    def test_voting_method_with_emulated_voting_method_instance(self):
        voting_method = VotingMethod.objects.get(pk=1)
        self.assertEqual(voting_method.name, "Majoritaire")
        self.assertEqual(voting_method.percentage, 0.5)
        voting_method = VotingMethod.objects.get(pk=2)
        self.assertEqual(voting_method.name, "Consensus75")
        self.assertEqual(voting_method.percentage, 0.75)
