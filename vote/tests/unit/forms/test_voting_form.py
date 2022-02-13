# pylint: disable=C0116
"""Test ratings form module.
"""
from django.test import TestCase

from vote.forms.voting_form import VotingForm
from vote.models.voting_method import VotingMethod
from vote.tests.unit.models.test_voting_method import VotingMethodTest


class VotingFormTest(TestCase):
    """Test VotingForm form  class.
    """
    def setUp(self):
        VotingMethodTest().emulate_voting_method()
        self.form = VotingForm()

    def test_vf_with_attr_question(self):
        self.assertEqual(self.form.fields['question'].label,'Question')
        self.assertEqual(self.form.fields['question'].max_length, 256)
        self.assertEqual(
            self.form.fields['question'].widget.attrs['id'],
            'input_voting_question'
        )
        self.assertEqual(
            self.form.fields['question'].widget.attrs['class'],
            'form-control form-control-sm'
        )

    def test_vf_with_attr_description(self):
        self.assertEqual(
            self.form.fields['description'].widget.attrs['id'],
            'input_voting_description'
        )
        self.assertEqual(self.form.fields['description'].label, 'Description')
        self.assertEqual(self.form.fields['description'].max_length, 1000)
        self.assertEqual(
            self.form.fields['description'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['description'].widget.attrs['rows'], 4
        )

    def test_vf_with_attr_opening_date(self):
        self.assertEqual(
            self.form.fields['opening_date'].widget.attrs['id'],
            'input_voting_opening_date'
        )
        self.assertEqual(
            self.form.fields['opening_date'].label, 'Date d\'ouverture du vote'
        )
        self.assertEqual(
            self.form.fields['opening_date'].widget.attrs['class'],
            'input-group date form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['closure_date']
            .widget.attrs['data-target-input'],
            'nearest'
        )

    def test_vf_with_attr_closure_date_id(self):
        self.assertEqual(
            self.form.fields['closure_date'].widget.attrs['id'],
            'input_voting_closure_date'
        )
        self.assertEqual(
            self.form.fields['closure_date'].label,
            'Date de fermeture du vote'
        )
        self.assertEqual(
            self.form.fields['closure_date'].widget.attrs['class'],
            'input-group date form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['closure_date']
            .widget.attrs['data-target-input'],
            'nearest'
        )

    def test_vf_with_attr_voting_method(self):
        self.assertEqual(
            self.form.fields['voting_method'].widget.attrs['id'],
            'input_voting_voting_method'
        )
        self.assertEqual(
            self.form.fields['voting_method'].label, 'Mode de scrutin'
        )
        self.assertEqual(
            self.form.fields['voting_method'].queryset[0],
            VotingMethod.objects.get(pk=1)
        )
        self.assertEqual(
            self.form.fields['voting_method'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        existing_index = None
        try:
            if self.voting_form.fields['voting_method'].widget.choices[3]:
                existing_index = True 
        except:
            existing_index = False
        self.assertFalse(existing_index)

    def test_vf_with_all_attr_are_correct(self):
        form = VotingForm(
            data={
                'question': 'Ma question est',
                'description': 'dsdss',
                'opening_date': "2022-01-02",
                'closure_date': "2022-01-25",
                'voting_method': VotingMethod.objects.get(pk=1).id
            }
        )
        self.assertTrue(form.is_valid())

    def test_vf_with_attr_question_is_empty(self):
        form = VotingForm(
            data={
                'question': '',
                'description': 'dsdss',
                'opening_date': "2022-01-02",
                'closure_date': "2022-01-25",
                'voting_method': VotingMethod.objects.get(pk=1).id
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_question_is_not_correct(self):
        form = VotingForm(
            data={
                'question': (
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    ),
                'description': 'dsdss',
                'opening_date': "2022-01-02",
                'closure_date': "2022-01-25",
                'voting_method': VotingMethod.objects.get(pk=1).id
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_description_is_empty(self):
        form = VotingForm(
            data={
                'question': 'Ma question est',
                'description': '',
                'opening_date': "2022-01-02",
                'closure_date': "2022-01-25",
                'voting_method': VotingMethod.objects.get(pk=1).id
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_description_is_not_correct(self):
        form = VotingForm(
            data={
                'question': 'Ma question est',
                'description': (
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                ),
                'opening_date': "2022-01-02",
                'closure_date': "2022-01-25",
                'voting_method': VotingMethod.objects.get(pk=1).id
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_opening_date_is_empty(self):
        form = VotingForm(
            data={
                'question': 'Ma question est',
                'description': 'dsdss',
                'opening_date': '',
                'closure_date': '2022-01-25',
                'voting_method': VotingMethod.objects.get(pk=1).id
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_opening_date_is_not_correct(self):
        form = VotingForm(
            data={
                'question': 'Ma question est',
                'description': 'dsdss',
                'opening_date': '01-02-2022',
                'closure_date': '2022-01-25',
                'voting_method': VotingMethod.objects.get(pk=1).id
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_closure_date_is_empty(self):
        form = VotingForm(
            data={
                'question': 'Ma question est',
                'description': 'dsdss',
                'opening_date': '2022-01-21',
                'closure_date': '',
                'voting_method': VotingMethod.objects.get(pk=1).id
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_closure_date_is_not_correct(self):
        form = VotingForm(
            data={
                'question': 'Ma question est',
                'description': 'dsdss',
                'opening_date': '2022-01-21',
                'closure_date': '01-02-2022',
                'voting_method': VotingMethod.objects.get(pk=1).id
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_voting_method_is_empty(self):
        form = VotingForm(
            data={
                'question': 'Ma question est',
                'description': 'dsdss',
                'opening_date': '2022-01-21',
                'closure_date': '2022-01-25',
                'voting_method': ''
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_voting_method_is_not_correct(self):
        form = VotingForm(
            data={
                'question': 'Ma question est',
                'description': 'dsdss',
                'opening_date': '2022-01-21',
                'closure_date': '2022-01-25',
                'voting_method': 4
            }
        )
        self.assertFalse(form.is_valid())
