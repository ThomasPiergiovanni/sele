# pylint: disable=C0116
"""Test ratings form module.
"""
from datetime import date

from django.test import TestCase

from vote.forms.add_voting import AddVoting


class AddVotingTest(TestCase):
    """Test AddVoting form  class.
    """
    def setUp(self):
        pass

    def test_add_voting_with_with_attr_question_wo_input(self):
        add_voting = AddVoting(data={
            'question': None,
            'description': 'dsdss',
            'creation_date':"2022-01-02"

        })
        self.assertFalse(add_voting.is_valid())

    def test_add_voting_with_with_attr_question_w_input(self):
        add_voting = AddVoting(data={
            'question': 'Ma question est',
            'description': 'dsdss',
            'creation_date': date(2022, 1, 11)
        })
        self.assertTrue(add_voting.is_valid())

    def test_add_voting_with_attr_question_ok_lenght(self):
        add_voting = AddVoting(data={
            'question': 'Ma question est la skdjskjskjdkjskdjksjdkjsjdkjkd'
            'lkslklklqkslqklskqlskqlkslkslkqlsklqkslsqlkslkqlsklqkslqklqkl',
            'description': 'dsdss',
            'creation_date':date(2022, 1, 11)
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
            'creation_date':date(2022, 1, 11)
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
            'creation_date':date(2022, 1, 11)
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
            'creation_date':date(2022, 1, 11)
        })
        self.assertFalse(add_voting.is_valid())

    def test_add_voting_with_attr_creation_date_wo_input(self):
        add_voting = AddVoting(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'creation_date' : None
        })
        self.assertFalse(add_voting.is_valid())

    def test_add_voting_with_attr_creation_date_w_input(self):
        add_voting = AddVoting(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'creation_date' : "2022-01-20"
        })
        self.assertTrue(add_voting.is_valid())

    def test_add_voting_with_attr_creation_date_w_incorrect_input(self):
        add_voting = AddVoting(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'creation_date' : "01-02-2022"
        })
        self.assertFalse(add_voting.is_valid())
