"""Test voting method module.
"""
from datetime import date
from django.db import models
from django.test import TestCase

from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.unit.models.test_voting_method import VotingMethodTest


class VotingTest(TestCase):
    """Test voting class.
    """
    def setUp(self):
        self.emulate_voting()

    def emulate_voting(self):
        """
        """
        VotingMethodTest().emulate_voting_method()
        Voting.objects.create(
            id=1,
            question="Voulez-vous créer une demande de nettoyage?",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
                " congue, euismod non, mi. Proin porttitor, orci nec nonummy"
                " molestie, enim est eleifend mi, non fermentum diam nisl sit"
                " amet erat. Duis semper. Duis arcu massa, scelerisque vitae,"
                " consequat in, pretium a, enim. Pellentesque congue"
            ),
            creation_date = "2022-01-10",
            opening_date = "2022-01-11",
            closure_date = "2022-01-19",
            voting_method_id=1
        )
        Voting.objects.create(
            id=2,
            question="Voulez-vous créer une offre commune d'aide au devoir?",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
                " congue, euismod non, mi. Proin porttitor, orci nec nonummy"
                " molestie, enim est eleifend mi, non fermentum diam nisl sit"
                " amet erat. Duis semper. Duis arcu massa, scelerisque vitae,"
                " consequat in, pretium a, enim. Pellentesque congue"
            ),
            creation_date = "2022-01-20",
            opening_date = "2022-01-21",
            closure_date = "2022-01-29",
            voting_method_id=2
        )

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
            type(models.ForeignKey(VotingMethod, models.CASCADE))
        )
    
    def test_status_with_emulated_status_instance(self):
        voting= Voting.objects.get(pk=1)
        self.assertEqual(
            voting.question,
            "Voulez-vous créer une demande de nettoyage?"
        )
        self.assertEqual(voting.opening_date, date(2022, 1, 11))
        voting = Voting.objects.get(pk=2)
        self.assertEqual(
            voting.question, 
            "Voulez-vous créer une offre commune d'aide au devoir?"
        )
        self.assertEqual(voting.opening_date, date(2022, 1, 21))
