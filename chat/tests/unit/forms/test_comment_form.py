# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from chat.forms.comment_form import CommentForm
from chat.tests.emulation.chat_emulation import ChatEmulation


class CommentFormTest(TestCase):

    def setUp(self):
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_test_setup()
        self.form = CommentForm()

    def test_cf_with_all_attr_subject(self):
        self.assertEqual(self.form.fields['comment'].label, 'Commenter')
        self.assertEqual(self.form.fields['comment'].max_length, 256)
        self.assertEqual(
            self.form.fields['comment'].widget.attrs['id'],
            'input_comment_comment'
        )
        self.assertEqual(
            self.form.fields['comment'].widget.attrs['class'],
            'form-control form-control-sm'
        )

    def test_cf_with_all_attr_are_correct(self):
        form = CommentForm(
            data={
                'comment': 'Alors???'
            }
        )
        self.assertTrue(form.is_valid())

    def test_cf_with_attr_subject_is_empty(self):
        form = CommentForm(
            data={
                'comment': ''
            }
        )
        self.assertFalse(form.is_valid())

    def test_cf_with_attr_subject_is_not_correct(self):
        form = CommentForm(
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
