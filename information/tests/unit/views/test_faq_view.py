# pylint: disable=C0116, W0212
"""Test faq view view module.
"""
from django.test import TestCase

from information.views.faq_view import FaqView


class TestFaqView(TestCase):
    """Test Faq view class.
    """
    def setUp(self):
        self.view = FaqView()

    def test_init_with_faq_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'information/faq.html')
        self.assertIsNone(self.view.context['questions'])
