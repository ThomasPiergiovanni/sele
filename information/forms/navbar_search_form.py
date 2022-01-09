"""Navigation search bar form module
"""
from django import forms


class NavbarSearchForm(forms.Form):
    """Navigation search bar form class. Used for searching user, group,
    propositions, votes, discussion with the navbar form
    """
    navbar_search_form = forms.CharField(
        label=None,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'id_navbar_search_form'
            }
        )
    )
