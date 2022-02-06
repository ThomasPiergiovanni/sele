# pylint: disable=C0116
"""Test ratings form module.
"""
from django.test import TestCase

from vote.forms.add_voting import AddVoting
from vote.models.voting_method import VotingMethod
from vote.tests.unit.models.test_voting_method import VotingMethodTest


class AddVotingTest(TestCase):
    """Test AddVoting form  class.
    """
    def setUp(self):
        VotingMethodTest().emulate_voting_method()
        self.add_voting = AddVoting()

    def test_add_voting_with_attr_question_label(self):
        self.assertEqual(
            self.add_voting.fields['question'].label,
            'Question'
        )
    def test_add_voting_with_attr_question_label(self):
        self.assertEqual(
            self.add_voting.fields['question'].max_length,
            256
        )

    def test_add_voting_with_attr_question_id(self):
        self.assertEqual(
            self.add_voting.fields['question'].widget.attrs['id'],
            'input_voting_question'
        )

    def test_add_voting_with_attr_question_class(self):
        self.assertEqual(
            self.add_voting.fields['question'].widget.attrs['class'],
            'form-control form-control-sm'
        )

    def test_add_voting_with_attr_description_id(self):
        self.assertEqual(
            self.add_voting.fields['description'].widget.attrs['id'],
            'input_voting_description'
        )

    def test_add_voting_with_attr_description_label(self):
        self.assertEqual(
            self.add_voting.fields['description'].label,
            'Description'
        )

    def test_add_voting_with_attr_description_max_lenght(self):
        self.assertEqual(
            self.add_voting.fields['description'].max_length,
            1000
        )

    def test_add_voting_with_attr_description_class(self):
        self.assertEqual(
            self.add_voting.fields['description'].widget.attrs['class'],
            'form-control form-control-sm'
        )

    def test_add_voting_with_attr_description_rows_class(self):
        self.assertEqual(
            self.add_voting.fields['description'].widget.attrs['rows'],
            4
        )

    def test_add_voting_with_attr_creation_date_id(self):
        self.assertEqual(
            self.add_voting.fields['creation_date'].widget.attrs['id'],
            'input_voting_creation_date'
        )

    def test_add_voting_with_attr_creation_date_label(self):
        self.assertEqual(
            self.add_voting.fields['creation_date'].label,
            'Date d\'ouverture du vote'
        )

    def test_add_voting_with_attr_creation_date_class(self):
        self.assertEqual(
            self.add_voting.fields['creation_date'].widget.attrs['class'],
            'input-group date form-control form-control-sm'
        )

    # def test_add_voting_with_attr_creation_date_type(self):
    #     self.assertEqual(
    #         self.add_voting.fields['creation_date'].widget.attrs['type'],
    #         'date'
    #     )
    
    def test_add_voting_with_attr_creation_date_data_target_input(self):
        self.assertEqual(
            self.add_voting.fields['creation_date']
            .widget.attrs['data-target-input'],
            'nearest'
        )

    def test_add_voting_with_attr_voting_method_id(self):
        self.assertEqual(
            self.add_voting.fields['voting_method'].widget.attrs['id'],
            'input_voting_voting_method'
        )

    def test_add_voting_with_attr_voting_method_label(self):
        self.assertEqual(
            self.add_voting.fields['voting_method'].label,
            'Mode de scrutin'
        )

    def test_add_voting_with_attr_voting_method_class(self):
        self.assertEqual(
            self.add_voting.fields['voting_method'].widget.attrs['class'],
            'form-control form-control-sm'
        )

    def test_add_voting_with_attr_voting_method_type(self):
        voting_method= VotingMethod.objects.all()
        self.assertEqual(
            self.add_voting.fields['voting_method'].widget.choices[0][0],
            voting_method[0].id
        )
