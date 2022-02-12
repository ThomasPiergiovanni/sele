# pylint: disable=C0116
"""Test ratings form module.
"""
from datetime import date
from operator import add

from django.test import TestCase

from vote.forms.add_voting import AddVoting
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.unit.models.test_voting_method import VotingMethodTest
from vote.tests.unit.models.test_voting import VotingTest


class AddVotingTest(TestCase):
    """Test AddVoting form  class.
    """
    def setUp(self):
        VotingMethodTest().emulate_voting_method()

    def test_add_voting_with_with_attr_question_wo_input(self):
        add_voting = AddVoting(data={
            'question': None,
            'description': 'dsdss',
            'opening_date':"2022-01-02",
            'voting_method': 1
        })
        self.assertFalse(add_voting.is_valid())

    def test_add_voting_with_attr_question_w_input(self):
        form_data = {
            'question': 'Ma question est',
            'description': 'dsdss',
            'opening_date': "2022-01-02",
            'voting_method': 1
        }
        add_voting = AddVoting(data=form_data)
        self.assertTrue(add_voting.is_valid())

    def test_add_voting_with_attr_question_ok_lenght(self):
        add_voting = AddVoting(data={
            'question': 'Ma question est la skdjskjskjdkjskdjksjdkjsjdkjkd'
            'lkslklklqkslqklskqlskqlkslkslkqlsklqkslsqlkslkqlsklqkslqklqkl',
            'description': 'dsdss',
            'opening_date':date(2022, 1, 11),
            'voting_method': 1
        })
        self.assertTrue(add_voting.is_valid())

    def test_add_voting_with_attr_question_over_lenght(self):
        add_voting = AddVoting(data={
            'question': 'Ma question est la skdjskjskjdkjskdjksjdkjsjdkjkd'
            'lkslklklqkslqklskqlskqlkslkslkqlsklqkslsqlkslkqlsklqkslqklqkl'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds',
            'description': 'dsdssdsdsdsdsdsdsdsdssdsds',
            'opening_date':date(2022, 1, 11),
            'voting_method': 1
        })
        self.assertFalse(add_voting.is_valid())

    def test_add_voting_with_with_attr_description_ok_lenght(self):
        add_voting = AddVoting(data={
            'question': 'Ma question est',
            'description': 'dsdssfdddddddfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd'
            'lkslklklqkslqklskqlskqlkslkslkqlsklqkslsqlkslkqlsklqkslqklqkl'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds',
            'opening_date':date(2022, 1, 11),
            'voting_method': 1,
        })
        self.assertTrue(add_voting.is_valid())

    def test_add_voting_with_with_attr_description_over_lenght(self):
        add_voting = AddVoting(data={
            'question': 'Ma question est',
            'description': 'dsdssfdddddddfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd'
            'lkslklklqkslqklskqlskqlkslkslkqlsklqkslsqlkslkqlsklqkslqklqkl'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'lkslklklqkslqklskqlskqlkslkslkqlsklqkslsqlkslkqlsklqkslqklqkl'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds',
            'opening_date':date(2022, 1, 11),
            'voting_method': 1
        })
        self.assertFalse(add_voting.is_valid())

    def test_add_voting_with_attr_creation_date_wo_input(self):
        add_voting = AddVoting(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'creation_date' : None,
            'voting_method': 1
        })
        self.assertFalse(add_voting.is_valid())

    def test_add_voting_with_attr_creation_date_w_input(self):
        add_voting = AddVoting(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'voting_method': 1
        })
        self.assertTrue(add_voting.is_valid())

    def test_add_voting_with_attr_creation_date_w_incorrect_input(self):
        add_voting = AddVoting(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "01-02-2022",
            'voting_method': 1
        })
        self.assertFalse(add_voting.is_valid())

    def test_add_voting_with_attr_voting_method_wo_input(self):
        add_voting = AddVoting(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'voting_method': None
        })
        self.assertFalse(add_voting.is_valid())

    def test_add_voting_with_attr_voting_method_w_input(self):
        add_voting = AddVoting(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'voting_method': 1
        })
        self.assertTrue(add_voting.is_valid())

    def test_add_voting_with_attr_voting_method_w_incorrect_input(self):
        add_voting = AddVoting(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'voting_method': "hgh"
        })
        self.assertFalse(add_voting.is_valid())
