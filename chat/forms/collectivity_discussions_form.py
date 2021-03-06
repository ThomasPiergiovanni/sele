"""Collectivity Discussions form module
"""
from django.forms import CharField, Form, TextInput


class CollectivityDiscussionsForm(Form):
    """CollectivityDiscussionsForm class. Used for searching Discussions
    page objects.
    """

    search_input = CharField(
        label='Rechercher',
        max_length=256,
        widget=TextInput(
            attrs={
                'id': 'input_search_discussion',
                'class': 'form-control form-control-sm',
                'autofocus': False,
            }
        )
    )
