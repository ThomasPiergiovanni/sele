# pylint: disable=C0116
"""Test collectivity voting form module.
"""
from django.test import TestCase

from vote.forms.collectivity_votings_form import CollectivityVotingsForm


class CollectivityVotingsFormTest(TestCase):
    """Test CollectivityVotinsForm   class.
    """
    def setUp(self):
        self.form = CollectivityVotingsForm()

    def test_cvf_with_attr_attrinute_selector(self):
        self.assertEqual(
            self.form.fields['attribute_selector'].label,'Trier par:'
        )
        self.assertEqual(
            self.form.fields['attribute_selector'].choices,
            [('question', 'Question'), ('date', 'Date de création')]
        )
        self.assertEqual(
            self.form.fields['attribute_selector'].widget.attrs['id'],
            'input_attribute_selector'
        )
        self.assertEqual(
            self.form.fields['attribute_selector'].widget.attrs['class'],
            'form-control form-control-sm'
        )

    def test_cvf_with_attr_order_selector(self):
        self.assertEqual(
            self.form.fields['order_selector'].label,'Dans l\'ordre:'
        )
        self.assertEqual(
            self.form.fields['order_selector'].choices,
            [('asc', 'Ascendant'), ('desc', 'Descendant')]
        )
        self.assertEqual(
            self.form.fields['order_selector'].widget.attrs['id'],
            'input_order_selector'
        )
        self.assertEqual(
            self.form.fields['order_selector'].widget.attrs['class'],
            'form-control form-control-sm'
        )

    def test_vf_with_all_attr_are_correct(self):
        form = CollectivityVotingsForm(
            data={
                'attribute_selector': 'question',
                'order_selector': 'desc',
            }
        )
        self.assertTrue(form.is_valid())
 