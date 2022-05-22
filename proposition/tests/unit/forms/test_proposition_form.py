# pylint: disable=C0114,C0115,C0116,E1101
from django.forms import (
    CharField, DateField, DateInput, IntegerField, ModelChoiceField,
    NumberInput, Select, Textarea, TextInput
)
from django.test import TestCase

from proposition.forms.proposition_form import PropositionForm
from proposition.models import (
    Category, CreatorType, Domain, Kind
)
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class PropositionFormTest(TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_test_setup()
        self.form = PropositionForm()

    def test_pf_with_attr_name(self):
        field = self.form.fields['name']
        self.assertTrue(field)
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.label, 'Intitulé')
        self.assertEqual(field.max_length, 128)
        self.assertIsInstance(field.widget, TextInput)
        self.assertEqual(field.widget.attrs['id'], 'input_proposition_name')
        self.assertEqual(
            field.widget.attrs['class'], 'form-control form-control-sm'
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
            field.widget.attrs['class'], 'form-control form-control-sm'
        )
        self.assertEqual(field.widget.attrs['rows'], 4)

    def test_pf_with_attr_proposition_kind(self):
        field = self.form.fields['proposition_kind']
        self.assertTrue(field)
        self.assertIsInstance(field, ModelChoiceField)
        self.assertEqual(field.label, 'Type de proposition (demande/offre)')
        self.assertIsInstance(field.widget, Select)
        self.assertEqual(
            field.widget.attrs['id'], 'input_proposition_proposition_kind'
        )
        self.assertEqual(
            field.widget.attrs['class'], 'form-control form-control-sm'
        )
        self.assertEqual(field.queryset[0], Kind.objects.get(pk=1))

    def test_pf_with_attr_proposition_category(self):
        field = self.form.fields['proposition_category']
        self.assertTrue(field)
        self.assertIsInstance(field, ModelChoiceField)
        self.assertEqual(field.label, 'Nature (activité/produit)')
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
            field.queryset[0], Domain.objects.get(pk=1)
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
            field.widget.attrs['data-target-input'], 'nearest'
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
            field.widget.attrs['data-target-input'], 'nearest'
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

    def test_pf_with_attr_proposition_creator_type(self):
        field = self.form.fields['proposition_creator_type']
        self.assertTrue(field)
        self.assertIsInstance(field, ModelChoiceField)
        self.assertEqual(field.label, 'Portée de la proposition')
        self.assertIsInstance(field.widget, Select)
        self.assertEqual(
            field.widget.attrs['id'],
            'input_proposition_proposition_creator_type'
        )
        self.assertEqual(
            field.widget.attrs['class'], 'form-control form-control-sm'
        )
        self.assertEqual(
            field.queryset[0], CreatorType.objects.get(pk=1)
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
                'duration': 60,
                'proposition_creator_type': CreatorType.objects.get(pk=2).id
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
                'duration': 60,
                'proposition_creator_type': CreatorType.objects.get(pk=2).id
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
                'duration': 60,
                'proposition_creator_type': CreatorType.objects.get(pk=2).id
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
                'duration': -60,
                'proposition_creator_type': CreatorType.objects.get(pk=2).id
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
                'duration': 14.2,
                'proposition_creator_type': CreatorType.objects.get(pk=2).id
            }
        )
        self.assertFalse(form.is_valid())

    def test_pf_with_attr_start_date_and_end_date_incorrect(self):
        form = PropositionForm(
            data={
                'name': 'J\'offre une heure de cours python',
                'description': 'dsdss',
                'proposition_kind': Kind.objects.get(pk=1).id,
                'proposition_category': Category.objects.get(pk=1).id,
                'proposition_domain': Domain.objects.get(pk=1).id,
                'start_date': "2022-01-30",
                'end_date': "2022-01-25",
                'duration': 14,
                'proposition_creator_type': CreatorType.objects.get(pk=2).id
            }
        )
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertEqual(
            form.errors.as_data()['__all__'][0].message,
            "Date de fin < Date de début"
        )

    def test_pf_with_attr_proposition_creator_type_incorrect(self):
        form = PropositionForm(
            data={
                'name': 'J\'offre une heure de cours python',
                'description': 'dsdss',
                'proposition_kind': Kind.objects.get(pk=2).id,
                'proposition_category': Category.objects.get(pk=1).id,
                'proposition_domain': Domain.objects.get(pk=1).id,
                'start_date': "2022-01-25",
                'end_date': "2022-01-30",
                'duration': 14,
                'proposition_creator_type': CreatorType.objects.get(pk=1).id
            }
        )
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertEqual(
            form.errors.as_data()['proposition_creator_type'][0].message,
            "Une offre ne peut pas être collective"
        )
