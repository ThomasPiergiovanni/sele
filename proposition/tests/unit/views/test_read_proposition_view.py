# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase

from proposition.views.read_proposition_view import ReadPropositionView


class ReadPropositionViewTest(TestCase):

    def setUp(self):
        self.view = ReadPropositionView()

    def test_init_with_read_proposition_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(
            self.view.view_template, 'proposition/read_proposition.html'
        )
        self.assertEqual(
            self.view.post_view_name, 'proposition:read_proposition'
        )
        self.assertEqual(
            ReadPropositionView.login_url, '/authentication/login/'
        )
        self.assertEqual(ReadPropositionView.redirect_field_name, None)
        self.assertIsNone(self.view.context)
