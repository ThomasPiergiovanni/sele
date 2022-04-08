"""Collectivity Propositions Search Form module 
"""
from django.forms import CharField, Form, TextInput


class CollectivityPropositionsSearchForm(Form):
    """CollectivityPropositionsSerachForm class. Used for sorting collectivity
    propositions page objects.
    """
    search_input = CharField(
        label='Rechercher (par id, nom, créateur ou preneur)',
        max_length=128,
        widget=TextInput(
            attrs={
                'id': 'input_search_input',
                'class': 'form-control form-control-sm',
                'autofocus': False,
            }
        )
    )