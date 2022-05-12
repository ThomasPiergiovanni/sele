# pylint: disable=C0116, W0212
"""Test contact view module.
"""
from django.test import TestCase

from information.views.contact_view import ContactView


class TestContactView(TestCase):
    """Test contact view class.
    """
    def setUp(self):
        self.view = ContactView()

    def test_init_with_about_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'information/contact.html')
