"""Collectivity Propositions Form module 
"""
from django.forms import ChoiceField, Form, Select


class CollectivityPropositionsForm(Form):
    """CollectivityPropositionsForm class. Used for sorting collectivity
    propositions page objects.
    """
    attribute_selector = ChoiceField(
        label='Trier par:',
        choices=(
            ('name', 'Nom'),
            ('proposition_kind', 'Type'),
            ('proposition_domain', 'Domaine'),
            ('duration', 'Temps de travail (minutes)'),
            ('proposition_status', 'Statut'),
            ('proposition_creator', 'Créateur'),
            ('proposition_taker', 'Preneur'),
            ('creation_date', 'Date de création')
        ),
        widget=Select(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_attribute_selector',
                'autofocus': False,
            }
        )
    )
    order_selector = ChoiceField(
        label='Dans l\'ordre:',
        choices=(('asc', 'Ascendant'), ('desc', 'Descendant')),
        widget=Select(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_order_selector',
                'autofocus': False,
            }
        )
    )
