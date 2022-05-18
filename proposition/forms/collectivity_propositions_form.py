"""CollectivityPropositionsForm (search form) module.
"""
from django.forms import CharField, Form, TextInput


class CollectivityPropositionsForm(Form):
    """CollectivityPropositionsForm (search form) class.
    """
    search_input = CharField(
        label='Rechercher',
        max_length=256,
        widget=TextInput(
            attrs={
                'id': 'input_search_proposition',
                'class': 'form-control form-control-sm',
                'autofocus': False,
            }
        )
    )
