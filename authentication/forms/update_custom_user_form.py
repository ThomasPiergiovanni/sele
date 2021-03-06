# pylint: disable=R0903,R0801
"""UpdateCustomUserForm module.
"""
from django import forms

from authentication.models import CustomUser


class UpdateCustomUserForm(forms.ModelForm):
    """UpdateCustomUserForm class.
    """

    user_name = forms.CharField(
        label="Nom d'utilisateur.rice",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-sm',
                'id': 'ecuf_input_user_name'
            }
        )
    )
    postal_code = forms.CharField(
        label='Code postal',
        max_length=5,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'autofocus': False,
                'class': 'form-control form-control-sm',
                'id': 'ecuf_input_postal_code',
            },
        )
    )
    collectivity = forms.CharField(
        label='Ville',
        max_length=256,
        widget=forms.TextInput(
            attrs={
                'autofocus': False,
                'class': 'form-control form-control-sm',
                'id': 'ecuf_input_collectivity',
            },
        )
    )
    field_order = ['user_name', 'postal_code', 'collectivity']

    class Meta:
        """Meta model gives CustomUser "params" to CreateCustomUser class.
        """

        model = CustomUser
        fields = ['user_name']
