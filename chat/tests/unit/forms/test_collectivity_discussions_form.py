# pylint: disable=C0116
"""Test collectivity discussions form module.
"""
from django.forms import CharField,TextInput
from django.test import TestCase

from chat.forms.collectivity_discussions_form import CollectivityDiscussionsForm


class CollectivityVotingsFormTest(TestCase):
    """Test CollectivityVotinsForm   class.
    """
    def setUp(self):
        self.form = CollectivityDiscussionsForm()

    def test_cvf_with_attr_search_input(self):
        field = self.form.fields['search_input']
        self.assertTrue(field)
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.label,'Rechercher')
        self.assertEqual(field.max_length, 256)
        self.assertIsInstance(field.widget, TextInput)
        self.assertEqual(field.widget.attrs['id'],'input_search_discussion')
        self.assertEqual(
            field.widget.attrs['class'],'form-control form-control-sm'
        )

    def test_cvf_with_all_attr_are_correct(self):
        form = CollectivityDiscussionsForm(
            data={
                'search_input': 'Une discussion sur ce sujet'
            }
        )
        self.assertTrue(form.is_valid())
 