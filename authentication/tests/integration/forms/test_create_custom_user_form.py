# pylint: disable=C0116
"""Test create custom user form module.
"""
from django.test import TestCase

from authentication.forms.create_custom_user_form import CreateCustomUserForm


class CreateCustomUserFormTest(TestCase):
    """Test CreateCustomUseForm  class.
    """
    def setUp(self):
        pass

    def test_ccuf_with_all_attr_are_correct(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name':'UserName',
            }
        )
        self.assertTrue(form.is_valid())

    def test_ccuf_with_attr_email_is_empty(self):
        form = CreateCustomUserForm(
            data={
                'email': '',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name':"UserName",
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_email_is_not_correct(self):
        form = CreateCustomUserForm(
            data={
                'email': 'useremail.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name':'UserName',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_password1_is_empty(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': '',
                'password2': 'xxxx_Xxxx',
                'user_name':"UserName",
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_password1_is_not_correct(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxxxxxx',
                'password2': 'xxxxxxxx',
                'user_name':"UserName",
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_password2_is_empty(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': '',
                'user_name':"UserName",
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_password2_is_not_correct(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Yxxx',
                'user_name':"UserName",
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_user_name_is_empty(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name': '',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_user_name_is_not_correct(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name':(
                    "dsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds"
                    "dsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds"
                )
            }
        )
        self.assertFalse(form.is_valid())

    