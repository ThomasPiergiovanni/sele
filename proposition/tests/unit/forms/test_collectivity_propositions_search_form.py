"""Test collectivity propositions search form module.
"""
from django.forms import (
    CharField, TextInput
)
from django.test import TestCase

from proposition.forms.collectivity_propositions_search_form import (
    CollectivityPropositionsSearchForm
)


class CollectivityPropositionsSearchFormTest(TestCase):
    """Test CollectivityPropositionsSearchForm class.
    """
    def setUp(self):
        self.form = CollectivityPropositionsSearchForm()

    def test_cpsf_with_attr_attribute_selector(self):
        field = self.form.fields['search_input']
        self.assertTrue(field)
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.label,'Rechercher')
        self.assertEqual(field.max_length, 256)
        self.assertIsInstance(field.widget, TextInput)
        self.assertEqual(field.widget.attrs['id'],'input_search_input')
        self.assertEqual(
            field.widget.attrs['class'],'form-control form-control-sm'
        )

    def test_vf_with_all_attr_are_correct(self):
        form = CollectivityPropositionsSearchForm(
            data={
                'search_input': 'Python'
            }
        )
        self.assertTrue(form.is_valid())
 