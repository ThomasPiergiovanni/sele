"""Test add voting view module.
"""
from django.test import TestCase

from authentication.views.edit_custom_user_view import EditCustomUserView


class EditCustomUserViewTest(TestCase):
    """TestEditCustomUserView view class.
    """
    def setUp(self):
        self.view =EditCustomUserView()

    def test_init_with_ecuv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr_nominal_template(self):
        self.assertEqual(
            self.view.get_nominal_template,
            'authentication/edit_custom_user.html'
        )
    def test_init_with_attr_alternative_tempate(self):
        self.assertEqual(
            self.view.get_alternative_template,
            'information/home.html'
        )
    def test_init_with_attr_post_nominal_view_name(self):
        self.assertEqual(
            self.view.post_nominal_view_name,
            'information:home'
        )
