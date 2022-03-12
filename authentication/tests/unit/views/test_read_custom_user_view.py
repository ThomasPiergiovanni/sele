"""Test read custom user view module.
"""
from django.test import TestCase

from authentication.views.read_custom_user_view import ReadCustomUserView


class ReadCustomUserViewTest(TestCase):
    """TestReadCustomUserView view class.
    """
    def setUp(self):
        self.view = ReadCustomUserView()

    def test_init_with_ecuv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr_view_template(self):
        self.assertEqual(
            self.view.view_template, 'authentication/read_custom_user.html'
        )

    def test_init_with_attr_alternative_view_name(self):
        self.assertEqual(
            self.view.alternative_view_name,'information:home'
        )
