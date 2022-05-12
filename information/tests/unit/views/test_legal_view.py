# pylint: disable=C0116, W0212
"""Test legal view module.
"""
from django.test import TestCase

from information.views.legal_view import LegalView


class TestLegalView(TestCase):
    """Test legal view class.
    """
    def setUp(self):
        self.view = LegalView()

    def test_init_with_about_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'information/legal.html')
