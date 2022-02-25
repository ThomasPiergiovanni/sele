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
            "Nom d'utilisateur.rice (visible dans l'app)"
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

    def test_ccuf_with_attr_postal_code(self):
        self.assertEqual(
            self.form.fields['postal_code'].label,
            "Code postal"
        )
        self.assertEqual(self.form.fields['postal_code'].max_length, 5)
        self.assertEqual(self.form.fields['postal_code'].min_length, 5)
        self.assertFalse(
            self.form.fields['postal_code'].widget.attrs['autofocus']
        )
        self.assertEqual(
            self.form.fields['postal_code'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['postal_code'].widget.attrs['id'],
            'input_postal_code'
        )


    def test_ccuf_with_all_attr_are_correct(self):
        """
        """
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
        self.assertTrue(form.is_valid())

    def test_ccuf_with_attr_email_is_empty(self):
        form = CreateCustomUserForm(
            data={
                'email': '',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code':'92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_email_is_not_correct(self):
        form = CreateCustomUserForm(
            data={
                'email': 'useremail.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code':'92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_password1_is_empty(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': '',
                'password2': 'xxxx_Xxxx',
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code':'92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_password1_is_not_correct(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxxxxxx',
                'password2': 'xxxx_Xxxx',
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code':'92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_password2_is_empty(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': '',
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code':'92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_password2_is_not_correct(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Yxxx',
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code':'92340',
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
                'collectivity': 'Bourg-la-Reine',
                'postal_code':'92340',
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
                ),
                'collectivity': 'Bourg-la-Reine',
                'postal_code':'92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_collectivity_is_empty(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name': 'UserName',
                'collectivity': '',
                'postal_code':'92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ccuf_with_attr_postal_code_is_empty(self):
        form = CreateCustomUserForm(
            data={
                'email': 'user@email.com',
                'password1': 'xxxx_Xxxx',
                'password2': 'xxxx_Xxxx',
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code': '',
            }
        )
        self.assertFalse(form.is_valid())
