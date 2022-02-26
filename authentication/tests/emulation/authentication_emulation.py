"""Test rating module.
"""
from authentication.forms.create_custom_user_form import CreateCustomUserForm


class AuthenticationEmulation():
    """Test collectivity class.
    """

    def emulate_custom_user_form(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code':'92340',
            }
        )
        return form
