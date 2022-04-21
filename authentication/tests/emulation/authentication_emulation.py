"""Test rating module.
"""
from django.contrib.auth.hashers import make_password

from authentication.forms.create_custom_user_form import CreateCustomUserForm
from authentication.models import CustomUser
from collectivity.models.collectivity import Collectivity
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)


class AuthenticationEmulation():
    """Test collectivity class.
    """
    def emulate_custom_user(self):
        """
        """
        CollectivityEmulation().emulate_postal_code()
        CollectivityEmulation().emulate_collectivity()
        CollectivityEmulation().emulate_set_collectivity_postal_code()
        blr = Collectivity.objects.get(name="Bourg-la-Reine")
        bgx = Collectivity.objects.get(name="Bagneux")
        CustomUser.objects.create(
            id=1,
            email="user1@email.com",
            password=make_password('xxx_Xxxx'),
            user_name="UserName1",
            balance=1000,
            collectivity_id=blr.id
        )
        CustomUser.objects.create(
            id=2,
            email="user2@email.com",
            password=make_password('yyy_Yyyy'),
            user_name="UserName2",
            balance=-2000,
            collectivity_id=bgx.id
        )
        CustomUser.objects.create(
            id=3,
            email="user3@email.com",
            password=make_password('xxx_Xxxx'),
            user_name="UserName3",
            balance=3000,
            collectivity_id=blr.id
        )

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

    def emulate_update_custom_user_form(self):
        form = CreateCustomUserForm(
            data={
                'user_name': 'UserNameNew',
                'collectivity': 'Bagneux',
                'postal_code':'9220',
            }
        )
        return form
