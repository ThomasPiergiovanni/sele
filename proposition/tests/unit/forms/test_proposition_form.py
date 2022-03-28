# pylint: disable=C0116
"""Test proposition form module.
"""
from django.test import TestCase

from authentication.models import CustomUser
from proposition.forms.proposition_form import PropositionForm
from proposition.models.category import Category
from proposition.models.creator_type import CreatorType
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.proposition import Proposition
from proposition.models.rating import Rating
from proposition.models.status import Status

from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class PropositionFormTest(TestCase):
    """Test PorpositionForm class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_proposition()
        self.form = PropositionForm()

    def test_vf_with_attr_name(self):
        self.assertEqual(self.form.fields['name'].label,'Intitulé')
        self.assertEqual(self.form.fields['name'].max_length, 128)
        self.assertEqual(
            self.form.fields['name'].widget.attrs['id'],
            'input_proposition_name'
        )
        self.assertEqual(
            self.form.fields['name'].widget.attrs['class'],
            'form-control form-control-sm'
        )


    def test_vf_with_attr_description(self):
        self.assertEqual(self.form.fields['description'].label, 'Description')
        self.assertEqual(
            self.form.fields['description'].widget.attrs['id'],
            'input_proposition_description'
        )
        self.assertEqual(self.form.fields['description'].max_length, 1000)
        self.assertEqual(
            self.form.fields['description'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['description'].widget.attrs['rows'], 4
        )

    def test_vf_with_attr_proposition_kind(self):
        self.assertEqual(
            self.form.fields['proposition_kind'].widget.attrs['id'],
            'input_proposition_proposition_kind'
        )
        self.assertEqual(
            self.form.fields['proposition_kind'].label,
            'Type de proposition (demande/offre)'
        )
        self.assertEqual(
            self.form.fields['proposition_kind'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['proposition_kind'].queryset[0],
            Kind.objects.get(pk=1)
        )

    # def test_vf_with_attr_closure_date_id(self):
    #     self.assertEqual(
    #         self.form.fields['closure_date'].widget.attrs['id'],
    #         'input_voting_closure_date'
    #     )
    #     self.assertEqual(
    #         self.form.fields['closure_date'].label,
    #         'Date de fermeture du vote'
    #     )
    #     self.assertEqual(
    #         self.form.fields['closure_date'].widget.attrs['class'],
    #         'input-group date form-control form-control-sm'
    #     )
    #     self.assertEqual(
    #         self.form.fields['closure_date']
    #         .widget.attrs['data-target-input'],
    #         'nearest'
    #     )

    # def test_vf_with_attr_voting_method(self):
    #     self.assertEqual(
    #         self.form.fields['voting_method'].widget.attrs['id'],
    #         'input_voting_voting_method'
    #     )
    #     self.assertEqual(
    #         self.form.fields['voting_method'].label, 'Mode de scrutin'
    #     )
    #     self.assertEqual(
    #         self.form.fields['voting_method'].queryset[0],
    #         VotingMethod.objects.get(pk=1)
    #     )
    #     self.assertEqual(
    #         self.form.fields['voting_method'].widget.attrs['class'],
    #         'form-control form-control-sm'
    #     )
    #     existing_index = None
    #     try:
    #         if self.voting_form.fields['voting_method'].widget.choices[3]:
    #             existing_index = True 
    #     except:
    #         existing_index = False
    #     self.assertFalse(existing_index)

    # def test_vf_with_all_attr_are_correct(self):
    #     form = VotingForm(
    #         data={
    #             'question': 'Ma question est',
    #             'description': 'dsdss',
    #             'opening_date': "2022-01-02",
    #             'closure_date': "2022-01-25",
    #             'voting_method': VotingMethod.objects.get(pk=1).id
    #         }
    #     )
    #     self.assertTrue(form.is_valid())

    # def test_vf_with_attr_question_is_empty(self):
    #     form = VotingForm(
    #         data={
    #             'question': '',
    #             'description': 'dsdss',
    #             'opening_date': "2022-01-02",
    #             'closure_date': "2022-01-25",
    #             'voting_method': VotingMethod.objects.get(pk=1).id
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_vf_with_attr_question_is_not_correct(self):
    #     form = VotingForm(
    #         data={
    #             'question': (
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 ),
    #             'description': 'dsdss',
    #             'opening_date': "2022-01-02",
    #             'closure_date': "2022-01-25",
    #             'voting_method': VotingMethod.objects.get(pk=1).id
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_vf_with_attr_description_is_empty(self):
    #     form = VotingForm(
    #         data={
    #             'question': 'Ma question est',
    #             'description': '',
    #             'opening_date': "2022-01-02",
    #             'closure_date': "2022-01-25",
    #             'voting_method': VotingMethod.objects.get(pk=1).id
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_vf_with_attr_description_is_not_correct(self):
    #     form = VotingForm(
    #         data={
    #             'question': 'Ma question est',
    #             'description': (
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #                 'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
    #             ),
    #             'opening_date': "2022-01-02",
    #             'closure_date': "2022-01-25",
    #             'voting_method': VotingMethod.objects.get(pk=1).id
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_vf_with_attr_opening_date_is_empty(self):
    #     form = VotingForm(
    #         data={
    #             'question': 'Ma question est',
    #             'description': 'dsdss',
    #             'opening_date': '',
    #             'closure_date': '2022-01-25',
    #             'voting_method': VotingMethod.objects.get(pk=1).id
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_vf_with_attr_opening_date_is_not_correct(self):
    #     form = VotingForm(
    #         data={
    #             'question': 'Ma question est',
    #             'description': 'dsdss',
    #             'opening_date': '01-02-2022',
    #             'closure_date': '2022-01-25',
    #             'voting_method': VotingMethod.objects.get(pk=1).id
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_vf_with_attr_closure_date_is_empty(self):
    #     form = VotingForm(
    #         data={
    #             'question': 'Ma question est',
    #             'description': 'dsdss',
    #             'opening_date': '2022-01-21',
    #             'closure_date': '',
    #             'voting_method': VotingMethod.objects.get(pk=1).id
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_vf_with_attr_closure_date_is_not_correct(self):
    #     form = VotingForm(
    #         data={
    #             'question': 'Ma question est',
    #             'description': 'dsdss',
    #             'opening_date': '2022-01-21',
    #             'closure_date': '01-02-2022',
    #             'voting_method': VotingMethod.objects.get(pk=1).id
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_vf_with_attr_voting_method_is_empty(self):
    #     form = VotingForm(
    #         data={
    #             'question': 'Ma question est',
    #             'description': 'dsdss',
    #             'opening_date': '2022-01-21',
    #             'closure_date': '2022-01-25',
    #             'voting_method': ''
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_vf_with_attr_voting_method_is_not_correct(self):
    #     form = VotingForm(
    #         data={
    #             'question': 'Ma question est',
    #             'description': 'dsdss',
    #             'opening_date': '2022-01-21',
    #             'closure_date': '2022-01-25',
    #             'voting_method': 4
    #         }
    #     )
    #     self.assertFalse(form.is_valid())
