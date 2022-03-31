"""Test collectivity propositions form module.
"""
from django.test import TestCase

from proposition.forms.collectivity_propositions_form import CollectivityPropositionsForm


class CollectivityPropositionsFormTest(TestCase):
    """Test CollectivityPropositionsForm class.
    """
    def setUp(self):
        self.form = CollectivityPropositionsForm()

    def test_cpf_with_attr_attribute_selector(self):
        self.assertEqual(
            self.form.fields['attribute_selector'].label,'Trier par:'
        )
        self.assertEqual(
            self.form.fields['attribute_selector'].choices,
            [
                ('name', 'Nom'),
                ('proposition_kind', 'Type'),
                ('duration', 'Temps de travail (minutes)'),
                ('proposition_status', 'Statut'),
                ('proposition_creator', 'Créateur'),
                ('proposition_taker', 'Preneur'),
                ('creation_date', 'Date de création')
            ]
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
        form = CollectivityPropositionsForm(
            data={
                'attribute_selector': 'duration',
                'order_selector': 'desc',
            }
        )
        self.assertTrue(form.is_valid())
 