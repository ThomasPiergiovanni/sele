# pylint: disable=C0114,C0115,C0116,E1101,R0201,R0801
from django.test import TestCase

from chat.forms.discussion_form import DiscussionForm
from chat.tests.emulation.chat_emulation import ChatEmulation


class DiscussionFormTest(TestCase):

    def setUp(self):
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_test_setup()
        self.form = DiscussionForm()

    def test_df_with_all_attr_subject(self):
        self.assertEqual(self.form.fields['subject'].label, 'Sujet')
        self.assertEqual(self.form.fields['subject'].max_length, 256)
        self.assertEqual(
            self.form.fields['subject'].widget.attrs['id'],
            'input_discussion_subject'
        )
        self.assertEqual(
            self.form.fields['subject'].widget.attrs['class'],
            'form-control form-control-sm'
        )

    def test_df_with_all_attr_are_correct(self):
        form = DiscussionForm(
            data={
                'subject': 'Ré-introduction de l\'ours en Mayenne'
            }
        )
        self.assertTrue(form.is_valid())

    def test_df_with_attr_subject_is_empty(self):
        form = DiscussionForm(
            data={
                'subject': ''
            }
        )
        self.assertFalse(form.is_valid())

    def test_vf_with_attr_subject_is_not_correct(self):
        form = DiscussionForm(
            data={
                'subject': (
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    'dsdsdsdsdsddsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd'
                    )
            }
        )
        self.assertFalse(form.is_valid())
