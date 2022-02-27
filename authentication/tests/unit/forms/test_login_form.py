# pylint: disable=C0116
"""Test ratings form module.
"""
from django.test import TestCase, RequestFactory

from authentication.forms.login_form import LoginForm
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from authentication.models import CustomUser


class LoginFormTest(TestCase):
    """Test CreateCustomUseForm  class.
    """
    def setUp(self):
        self.form = LoginForm()

    def test_lf_with_attr_email(self):
        self.assertEqual(
            self.form.fields['username'].label, "Email"
        )
        self.assertEqual(self.form.fields['username'].max_length, 128)
        self.assertTrue(self.form.fields['username'].widget.attrs['autofocus'])
        self.assertEqual(
            self.form.fields['username'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['username'].widget.attrs['id'],
            'input_login_email'
        )

    def test_lf_with_attr_password(self):
        self.assertEqual(self.form.fields['password'].label,"Mot de passe")
        self.assertEqual(self.form.fields['password'].max_length, 32)
        self.assertFalse(self.form.fields['password'].widget.attrs['autofocus'])
        self.assertEqual(
            self.form.fields['password'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['password'].widget.attrs['id'],
            'input_login_password'
        )

    def test_lf_with_all_attr_are_correct(self):
        """
        """
        AuthenticationEmulation().emulate_custom_user()
        data = {
            'username': 'user1@email.com',
            'password': 'xxx_Xxxx'
        }

        form = LoginForm(data=data)
        print(form.data['username'])
        self.assertTrue(form.is_valid())  

    # def test_lf_with_attr_email_is_empty(self):
    #     form = LoginForm(
    #         data={
    #             'email': '',
    #             'password': 'xxx_Xxxxx',
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_lf_with_attr_email_is_not_correct(self):
    #     form = LoginForm(
    #         data={
    #             'email': 'useremail.com',
    #             'password1': 'xxx_Xxxxx',
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_lf_with_attr_password_is_empty(self):
    #     form = LoginForm(
    #         data={
    #             'email': 'user1@email.com',
    #             'password1': '',
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

    # def test_lf_with_attr_password1_is_not_correct(self):
    #     form = LoginForm(
    #         data={
    #             'email': 'user1@email.com',
    #             'password1': 'xxxxxxxx',
    #         }
    #     )
    #     self.assertFalse(form.is_valid())

