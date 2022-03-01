"""Login form module.
"""
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    """Login form class.
    """
    username = forms.CharField(
        label="Email",
        max_length=128,
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-sm',
                'id': 'input_login_email',
            }
        )
    )
    password = forms.CharField(
        label="Mot de passe",
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'autofocus': False,
                'class': 'form-control form-control-sm',
                'id': 'input_login_password'
            }
        )
    )
    # field_order = ['email', 'password'] 

    # class Meta(AuthenticationForm):
    #     """Meta model gives CustomUser "params" to CreateCustomUser class.
    #     """
    #     model = CustomUser
    #     fields = ['email', 'password']
