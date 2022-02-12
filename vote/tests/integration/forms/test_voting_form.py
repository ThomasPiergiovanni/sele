# pylint: disable=C0116
"""Test ratings form module.
"""
from datetime import date
from operator import add

from django.test import TestCase

from vote.forms.voting_form import VotingForm
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.unit.models.test_voting_method import VotingMethodTest
from vote.tests.unit.models.test_voting import VotingTest


class VotingFormTest(TestCase):
    """Test VotingForm form  class.
    """
    def setUp(self):
        VotingMethodTest().emulate_voting_method()

    def test_voting_form_with_with_attr_question_wo_input(self):
        voting_form = VotingForm(data={
            'question': None,
            'description': 'dsdss',
            'opening_date':"2022-01-02",
            'closure_date': "2022-01-25",
            'voting_method': 1
        })
        self.assertFalse(voting_form.is_valid())

    def test_voting_form_with_attr_question_w_input(self):
        form_data = {
            'question': 'Ma question est',
            'description': 'dsdss',
            'opening_date': "2022-01-02",
            'closure_date': "2022-01-25",
            'voting_method': 1
        }
        voting_form = VotingForm(data=form_data)
        self.assertTrue(voting_form.is_valid())

    def test_voting_form_with_attr_question_ok_lenght(self):
        voting_form = VotingForm(data={
            'question': 'Ma question est la skdjskjskjdkjskdjksjdkjsjdkjkd'
            'lkslklklqkslqklskqlskqlkslkslkqlsklqkslsqlkslkqlsklqkslqklqkl',
            'description': 'dsdss',
            'opening_date':"2022-01-02",
            'closure_date': "2022-01-25",
            'voting_method': 1
        })
        self.assertTrue(voting_form.is_valid())

    def test_voting_form_with_attr_question_over_lenght(self):
        voting_form = VotingForm(data={
            'question': 'Ma question est la skdjskjskjdkjskdjksjdkjsjdkjkd'
            'lkslklklqkslqklskqlskqlkslkslkqlsklqkslsqlkslkqlsklqkslqklqkl'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds'
            'sklqkslkqlkslqkdlskdlksldklskdlkslkdlskdlkslkdksldklskdlkskds',
            'description': 'dsdssdsdsdsdsdsdsdsdssdsds',
            'opening_date':"2022-01-02",
            'closure_date': "2022-01-25",
            'voting_method': 1
        })
        self.assertFalse(voting_form.is_valid())

    def test_voting_form_with_with_attr_description_ok_lenght(self):
        voting_form = VotingForm(data={
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
            'closure_date': "2022-01-25",
            'voting_method': 1,
        })
        self.assertTrue(voting_form.is_valid())

    def test_voting_form_with_with_attr_description_over_lenght(self):
        voting_form = VotingForm(data={
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
            'closure_date': "2022-01-25",
            'voting_method': 1
        })
        self.assertFalse(voting_form.is_valid())

    def test_voting_form_with_attr_opening_date_wo_input(self):
        voting_form = VotingForm(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : None,
            'closure_date': "2022-01-25",
            'voting_method': 1
        })
        self.assertFalse(voting_form.is_valid())

    def test_voting_form_with_attr_opening_date_w_input(self):
        voting_form = VotingForm(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'closure_date': "2022-01-25",
            'voting_method': 1
        })
        self.assertTrue(voting_form.is_valid())

    def test_voting_form_with_attr_opening_date_w_incorrect_input(self):
        voting_form = VotingForm(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "01-02-2022",
            'closure_date': "2022-01-25",
            'voting_method': 1
        })
        self.assertFalse(voting_form.is_valid())

    def test_voting_form_with_attr_closure_date_wo_input(self):
        voting_form = VotingForm(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'closure_date': None,
            'voting_method': 1
        })
        self.assertFalse(voting_form.is_valid())

    def test_voting_form_with_attr_closure_date_w_input(self):
        voting_form = VotingForm(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'closure_date': "2022-01-25",
            'voting_method': 1
        })
        self.assertTrue(voting_form.is_valid())

    def test_voting_form_with_attr_closure_date_w_incorrect_input(self):
        voting_form = VotingForm(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'closure_date': "01-02-2022",
            'voting_method': 1
        })
        self.assertFalse(voting_form.is_valid())

    def test_voting_form_with_attr_voting_method_wo_input(self):
        voting_form = VotingForm(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'closure_date': "2022-02-15",
            'voting_method': None
        })
        self.assertFalse(voting_form.is_valid())

    def test_voting_form_with_attr_voting_method_w_input(self):
        voting_form = VotingForm(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'closure_date': "2022-01-25",
            'voting_method': 1
        })
        self.assertTrue(voting_form.is_valid())

    def test_voting_form_with_attr_voting_method_w_incorrect_input(self):
        voting_form = VotingForm(data={
            'question': 'dsdsdsd',
            'description': 'dsdss',
            'opening_date' : "2022-01-20",
            'closure_date': "2022-01-25",
            'voting_method': "hgh"
        })
        self.assertFalse(voting_form.is_valid())
