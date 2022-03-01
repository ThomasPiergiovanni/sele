"""Sign up form module.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm


from authentication.models import CustomUser
from collectivity.models.collectivity import Collectivity


class EditCustomUserForm(forms.ModelForm):
    """Edit CustomUser form class.
    """
    user_name = forms.CharField(
        label="Nom d'utilisateur.rice (visible dans l'app)",
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
    field_order = ['user_name', 'postal_code','collectivity'] 

    class Meta(UserCreationForm):
        """Meta model gives CustomUser "params" to CreateCustomUser class.
        """
        model = CustomUser
        fields = ['user_name']
