"""Test add voting view module.
"""
from django.test import TestCase

from authentication.views.update_custom_user_view import UpdateCustomUserView


class UpdateCustomUserViewTest(TestCase):
    """TestUpdateCustomUserView view class.
    """
    def setUp(self):
        self.view =UpdateCustomUserView()

    def test_init_with_ecuv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr_nominal_template(self):
        self.assertEqual(
            self.view.view_template,
            'authentication/update_custom_user.html'
        )
    def test_init_with_attr_alternative_view_name(self):
        self.assertEqual(
            self.view.alternative_view_name,
            'information:home'
        )
