"""Test manager module.
"""
from django.test import TestCase

from authentication.forms.create_custom_user_form import CreateCustomUserForm
from authentication.management.engine.manager import Manager
from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import CustomUserTest


class TestManager(TestCase):
    """Test Manager  class.
    """
    def setUp(self):
        pass
        # CustomUserTest().emulate_custom_user()
        # self.manager = Manager()

    # def test_create_custom_user_with_custom_user_instance(self):
    #     form_data = {
    #         'email': 'user@email.com',
    #         'password1': 'xxxx_Xxxx',
    #         'password2': 'xxxx_Xxxx',
    #         'user_name': 'UserName',
    #         'postal_code': '92340',
    #     }
    #     form = CreateCustomUserForm(data=form_data)
    #     form.is_valid()
    #     self.manager.create_custom_user(form)
    #     self.assertEqual(
    #         CustomUser.objects.all().order_by('-id')[0].email,
    #         'user@email.com'
    #     )
