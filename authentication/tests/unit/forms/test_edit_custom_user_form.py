# pylint: disable=C0114,C0115,C0116,E1101,R0801
from django.test import TestCase

from authentication.forms.update_custom_user_form import UpdateCustomUserForm


class UpdateCustomUserFormTest(TestCase):

    def setUp(self):
        self.form = UpdateCustomUserForm()

    def test_ecuf_with_attr_user_name(self):
        self.assertEqual(
            self.form.fields['user_name'].label,
            "Nom d'utilisateur.rice"
        )
        self.assertEqual(self.form.fields['user_name'].max_length, 64)
        self.assertTrue(
            self.form.fields['user_name'].widget.attrs['autofocus']
        )
        self.assertEqual(
            self.form.fields['user_name'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['user_name'].widget.attrs['id'],
            'ecuf_input_user_name'
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
            'ecuf_input_postal_code'
        )

    def test_ecuf_with_attr_collectivity(self):
        self.assertEqual(
            self.form.fields['collectivity'].label,
            "Ville"
        )
        self.assertEqual(self.form.fields['collectivity'].max_length, 256)
        self.assertFalse(
            self.form.fields['collectivity'].widget.attrs['autofocus']
        )
        self.assertEqual(
            self.form.fields['collectivity'].widget.attrs['class'],
            'form-control form-control-sm'
        )
        self.assertEqual(
            self.form.fields['collectivity'].widget.attrs['id'],
            'ecuf_input_collectivity'
        )

    def test_ecuf_with_all_attr_are_correct(self):
        form = UpdateCustomUserForm(
            data={
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code': '92340',
            }
        )
        self.assertTrue(form.is_valid())

    def test_ecuf_with_attr_user_name_is_empty(self):
        form = UpdateCustomUserForm(
            data={
                'user_name': '',
                'collectivity': 'Bourg-la-Reine',
                'postal_code': '92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ecuf_with_attr_user_name_is_not_correct(self):
        form = UpdateCustomUserForm(
            data={
                'user_name': (
                    "dsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds"
                    "dsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds"
                ),
                'collectivity': 'Bourg-la-Reine',
                'postal_code': '92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ecuf_with_attr_collectivity_is_empty(self):
        form = UpdateCustomUserForm(
            data={
                'user_name': 'UserName',
                'collectivity': '',
                'postal_code': '92340',
            }
        )
        self.assertFalse(form.is_valid())

    def test_ecuf_with_attr_postal_code_is_empty(self):
        form = UpdateCustomUserForm(
            data={
                'user_name': 'UserName',
                'collectivity': 'Bourg-la-Reine',
                'postal_code': '',
            }
        )
        self.assertFalse(form.is_valid())
