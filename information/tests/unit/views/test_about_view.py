# pylint: disable=C0116, W0212
"""Test about view module.
"""
from django.test import TestCase

from information.views.about_view import AboutView


class TestAboutView(TestCase):
    """Test about view class.
    """
    def setUp(self):
        self.view = AboutView()

    def test_init_with_about_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'information/about.html')
