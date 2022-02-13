"""Sign up form module.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm

from authentication.models import CustomUser


class CreateCustomUserForm(UserCreationForm):
    """Sign up form class.
    """
    email = forms.CharField(
        label="Email (identifiant)",
        max_length=128,
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-sm',
                'id': 'input_custom_user_email',
            }
        )
    )
    user_name = forms.CharField(
        label="Nom d'utilisateur.rice (nom visible dans l'app)",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'autofocus': False,
                'class': 'form-control form-control-sm',
                'id': 'input_custom_user_user_name'
            }
        )
    )
    password1 = forms.CharField(
        label="Mot de passe",
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'autofocus': False,
                'class': 'form-control form-control-sm',
                'id': 'input_custom_user_password1'
            }
        )
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'autofocus': False,
                'class': 'form-control form-control-sm',
                'id': 'input_custom_user_password2'
            }
        )
    )


    class Meta(UserCreationForm):
        """Meta model gives CustomUser "params" to CreateCustomUser class.
        """
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'user_name',]
