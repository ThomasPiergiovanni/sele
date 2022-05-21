# pylint: disable=C0114,C0115,C0116,E1101
from django.forms import CharField, TextInput
from django.test import TestCase

from proposition.forms.collectivity_propositions_form import (
    CollectivityPropositionsForm
)


class CollectivityPropositionsFormTest(TestCase):

    def setUp(self):
        self.form = CollectivityPropositionsForm()

    def test_cpf_with_attr_search_input(self):
        field = self.form.fields['search_input']
        self.assertTrue(field)
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.label, 'Rechercher')
        self.assertEqual(field.max_length, 256)
        self.assertIsInstance(field.widget, TextInput)
        self.assertEqual(field.widget.attrs['id'], 'input_search_proposition')
        self.assertEqual(
            field.widget.attrs['class'], 'form-control form-control-sm'
        )

    def test_cpf_with_all_attr_are_correct(self):
        form = CollectivityPropositionsForm(
            data={
                'search_input': 'Python'
            }
        )
        self.assertTrue(form.is_valid())
