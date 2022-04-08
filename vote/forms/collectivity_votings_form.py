"""Collectivity Voting Form module 
"""
from django.forms import CharField, Form, TextInput


class CollectivityVotingsForm(Form):
    """CollectivityVotingsForm class. Used for sorting collectivity votings
    page objects.
    """
    search_input = CharField(
        label='Rechercher',
        max_length=256,
        widget=TextInput(
            attrs={
                'id': 'input_search_input',
                'class': 'form-control form-control-sm',
                'autofocus': False,
            }
        )
    )
