# pylint: disable=C0116
"""Test proposition form module.
"""
from calendar import TextCalendar
from django.forms import (
    CharField, DateField, DateInput, IntegerField, ModelChoiceField,
    NumberInput, Select, Textarea, 
    TextInput
)
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

    def test_pf_with_attr_name(self):
        field = self.form.fields['name']
        self.assertTrue(field)
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.label,'Intitulé')
        self.assertEqual(field.max_length, 128)
        self.assertIsInstance(field.widget, TextInput)
        self.assertEqual(field.widget.attrs['id'],'input_proposition_name')
        self.assertEqual(
            field.widget.attrs['class'],'form-control form-control-sm'
        )


    def test_pf_with_attr_description(self):
        field = self.form.fields['description']
        self.assertTrue(field)
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.label, 'Description')
        self.assertEqual(
            field.widget.attrs['id'], 'input_proposition_description'
        )
        self.assertEqual(field.max_length, 1000)
        self.assertIsInstance(field.widget, Textarea)
        self.assertEqual(
            field.widget.attrs['class'],'form-control form-control-sm'
        )
        self.assertEqual(field.widget.attrs['rows'], 4)

    def test_pf_with_attr_proposition_kind(self):
        field = self.form.fields['proposition_kind']
        self.assertTrue(field)
        self.assertIsInstance(field, ModelChoiceField)
        self.assertEqual(field.label,'Type de proposition (demande/offre)')
        self.assertIsInstance(field.widget, Select)
        self.assertEqual(
            field.widget.attrs['id'], 'input_proposition_proposition_kind'
        )
        self.assertEqual(
            field.widget.attrs['class'], 'form-control form-control-sm'
        )
        self.assertEqual(field.queryset[0],Kind.objects.get(pk=1))

    def test_pf_with_attr_proposition_category(self):
        field = self.form.fields['proposition_category']
        self.assertTrue(field)
        self.assertIsInstance(field, ModelChoiceField)
        self.assertEqual(field.label, 'Nature')
        self.assertIsInstance(field.widget, Select)
        self.assertEqual(
            field.widget.attrs['id'],
            'input_proposition_proposition_category'
        )
        self.assertEqual(
            field.widget.attrs['class'], 'form-control form-control-sm'
        )
        self.assertEqual(
            field.queryset[0], Category.objects.get(pk=1)
        )

    def test_pf_with_attr_proposition_domain(self):
        field = self.form.fields['proposition_domain']
        self.assertTrue(field)
        self.assertIsInstance(field, ModelChoiceField)
        self.assertEqual(field.label, 'Domaine')
        self.assertIsInstance(field.widget, Select)
        self.assertEqual(
            field.widget.attrs['id'],
            'input_proposition_proposition_domain'
        )
        self.assertEqual(
            field.widget.attrs['class'], 'form-control form-control-sm'
        )
        self.assertEqual(
            field.queryset[0],Domain.objects.get(pk=1)
        )

    def test_pf_with_attr_start_date(self):
        field = self.form.fields['start_date']
        self.assertTrue(field)
        self.assertIsInstance(field, DateField)
        self.assertEqual(field.label, 'Date de début de proposition')
        self.assertIsInstance(field.widget, DateInput)
        self.assertEqual(
            field.widget.attrs['id'], 'input_proposition_start_date'
        )
        self.assertEqual(
            field.widget.attrs['class'],
            'input-group date form-control form-control-sm'
        )
        self.assertEqual(
            field.widget.attrs['data-target-input'],'nearest'
        )
    def test_pf_with_attr_end_date(self):
        field = self.form.fields['end_date']
        self.assertTrue(field)
        self.assertIsInstance(field, DateField)
        self.assertEqual(field.label, 'Date de fin de proposition')
        self.assertIsInstance(field.widget, DateInput)
        self.assertEqual(
            field.widget.attrs['id'],
            'input_proposition_end_date'
        )
        self.assertEqual(
            field.widget.attrs['class'],
            'input-group date form-control form-control-sm'
        )
        self.assertEqual(
            field.widget.attrs['data-target-input'],'nearest'
        )

    def test_pf_with_attr_duration(self):
        field = self.form.fields['duration']
        self.assertTrue(field)
        self.assertIsInstance(field, IntegerField)
        self.assertEqual(field.label, 'Temps de travail (minutes)')
        self.assertEqual(field.min_value, 1)
        self.assertIsInstance(field.widget, NumberInput)
        self.assertEqual(
            field.widget.attrs['id'],
            'input_proposition_duration'
        )
        self.assertEqual(
            field.widget.attrs['class'],
            'form-control form-control-sm'
        )



    def test_pf_with_all_attr_are_correct(self):
        form = PropositionForm(
            data={
                'name': 'J\'offre une heure de cours python',
                'description': 'dsdss',
                'proposition_kind': Kind.objects.get(pk=1).id,
                'proposition_category': Category.objects.get(pk=1).id,
                'proposition_domain': Domain.objects.get(pk=1).id,
                'start_date': "2022-01-25",
                'end_date': "2022-01-30",
                'duration':60
            }
        )
        self.assertTrue(form.is_valid())

    def test_pf_with_attr_are_description_is_empty(self):
        form = PropositionForm(
            data={
                'name': 'J\'offre une heure de cours python',
                'description': '',
                'proposition_kind': Kind.objects.get(pk=1).id,
                'proposition_category': Category.objects.get(pk=1).id,
                'proposition_domain': Domain.objects.get(pk=1).id,
                'start_date': "2022-01-25",
                'end_date': "2022-01-30",
                'duration':60
            }
        )
        self.assertFalse(form.is_valid())

    def test_pf_with_attr_are_start_date_is_incorrect(self):
        form = PropositionForm(
            data={
                'name': 'J\'offre une heure de cours python',
                'description': 'dsdss',
                'proposition_kind': Kind.objects.get(pk=1).id,
                'proposition_category': Category.objects.get(pk=1).id,
                'proposition_domain': Domain.objects.get(pk=1).id,
                'start_date': "2022-01-32",
                'end_date': "2022-01-30",
                'duration':60
            }
        )
        self.assertFalse(form.is_valid())

    def test_pf_with_attr_are_start_duration_is_incorrect_neg(self):
        form = PropositionForm(
            data={
                'name': 'J\'offre une heure de cours python',
                'description': 'dsdss',
                'proposition_kind': Kind.objects.get(pk=1).id,
                'proposition_category': Category.objects.get(pk=1).id,
                'proposition_domain': Domain.objects.get(pk=1).id,
                'start_date': "2022-01-25",
                'end_date': "2022-01-30",
                'duration':-60
            }
        )
        self.assertFalse(form.is_valid())

    def test_pf_with_attr_are_start_duration_is_incorrect_float(self):
        form = PropositionForm(
            data={
                'name': 'J\'offre une heure de cours python',
                'description': 'dsdss',
                'proposition_kind': Kind.objects.get(pk=1).id,
                'proposition_category': Category.objects.get(pk=1).id,
                'proposition_domain': Domain.objects.get(pk=1).id,
                'start_date': "2022-01-25",
                'end_date': "2022-01-30",
                'duration':14.2
            }
        )
        self.assertFalse(form.is_valid())

    def test_pf_with_attr_are_end_start_incorrect(self):
        form = PropositionForm(
            data={
                'name': 'J\'offre une heure de cours python',
                'description': 'dsdss',
                'proposition_kind': Kind.objects.get(pk=1).id,
                'proposition_category': Category.objects.get(pk=1).id,
                'proposition_domain': Domain.objects.get(pk=1).id,
                'start_date': "2022-01-30",
                'end_date': "2022-01-25",
                'duration':14
            }
        )
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)        
        self.assertEqual(
            form.errors.as_data()['__all__'][0].message,
            "Date de fin < Date de début"
        )
