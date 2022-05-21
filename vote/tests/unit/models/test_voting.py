# pylint: disable=C0114,C0115,C0116,E1101,W0212
from datetime import date
from django.db import models
from django.test import TestCase

from authentication.models import CustomUser
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.emulation.vote_emulation import VoteEmulation


class VotingTest(TestCase):

    def setUp(self):
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_test_setup()

    def test_voting_with_status_class(self):
        voting = Voting.objects.get(pk=1)
        self.assertIsInstance(voting, Voting)

    def test_voting_with_attr_name_characteristic(self):
        attribute = Voting._meta.get_field('question')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 256)
        self.assertEqual(attribute.unique, False)

    def test_voting_with_attr_decsription_characteristic(self):
        attribute = Voting._meta.get_field('description')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.TextField()))
        self.assertEqual(attribute.max_length, 1000)
        self.assertEqual(attribute.unique, False)

    def test_voting_with_attr_creation_date_characteristic(self):
        attribute = Voting._meta.get_field('creation_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateField()))

    def test_voting_with_attr_opening_date_characteristic(self):
        attribute = Voting._meta.get_field('opening_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateField()))

    def test_voting_with_attr_closure_date_characteristic(self):
        attribute = Voting._meta.get_field('closure_date')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.DateField()))

    def test_voting_with_attr_voting_method_characteristic(self):
        attribute = Voting._meta.get_field('voting_method')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(VotingMethod, on_delete=models.CASCADE))
        )

    def test_voting_with_attr_voting_custom_user_characteristic(self):
        attribute = Voting._meta.get_field('voting_custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, on_delete=models.CASCADE))
        )

    def test_voting_with_attr_votes_characteristic(self):
        attribute = Voting._meta.get_field('votes')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ManyToManyField(CustomUser))
        )

    def test_status_with_emulated_status_instance(self):
        voting = Voting.objects.get(pk=1)
        self.assertEqual(
            voting.question,
            "Voulez-vous créer une demande de nettoyage?"
        )
        self.assertEqual(voting.opening_date, date.today())
        voting = Voting.objects.get(pk=2)
        self.assertEqual(
            voting.question,
            "Voulez-vous créer une offre commune d'aide au devoir?"
        )
        self.assertEqual(voting.opening_date, date(2022, 1, 21))
