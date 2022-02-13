# pylint: disable=C0116
"""Test ratings form module.
"""
from django.test import TestCase

from authentication.forms.create_custom_user_form import CreateCustomUserForm


class CreateCustomUserFormTest(TestCase):
    """Test CreateCustomUseForm  class.
    """
    def setUp(self):
        self.form = CreateCustomUserForm()

    def test_ccuf_with_attr_email(self):
        self.assertEqual(
            self.form.fields['email'].label, "Email (identifiant)"
        )
        self.assertEqual(self.form.fields['email'].max_length, 128)
        self.assertTrue(self.form.fields['email'].widget.attrs['autofocus'])
        self.assertEqual(
            self.form.fields['email'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['email'].widget.attrs['id'],
            'input_custom_user_email'
        )

    def test_ccuf_with_attr_user_name(self):
        self.assertEqual(
            self.form.fields['user_name'].label,
            "Nom d'utilisateur.rice (nom visible dans l'app)"
        )
        self.assertEqual(self.form.fields['user_name'].max_length, 64)
        self.assertFalse(self.form.fields['user_name'].widget.attrs['autofocus'])
        self.assertEqual(
            self.form.fields['user_name'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['user_name'].widget.attrs['id'],
            'input_custom_user_user_name'
        )

    def test_ccuf_with_attr_password1(self):
        self.assertEqual(self.form.fields['password1'].label,"Mot de passe")
        self.assertEqual(self.form.fields['password1'].max_length, 32)
        self.assertFalse(self.form.fields['password1'].widget.attrs['autofocus'])
        self.assertEqual(
            self.form.fields['password1'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['password1'].widget.attrs['id'],
            'input_custom_user_password1'
        )

    def test_ccuf_with_attr_password2(self):
        self.assertEqual(
            self.form.fields['password2'].label, "Confirmer le mot de passe"
        )
        self.assertEqual(self.form.fields['password2'].max_length, 32)
        self.assertFalse(
            self.form.fields['password2'].widget.attrs['autofocus']
        )
        self.assertEqual(
            self.form.fields['password2'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['password2'].widget.attrs['id'],
            'input_custom_user_password2'
        )
