# pylint: disable=C0114,C0115,C0116,W0212
from django.test import TestCase

from information.views.legal_view import LegalView


class TestLegalView(TestCase):

    def setUp(self):
        self.view = LegalView()

    def test_init_with_about_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template, 'information/legal.html')
