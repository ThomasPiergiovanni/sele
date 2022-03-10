"""Test add voting view module.
"""
from django.test import TestCase
from django.urls import reverse

from authentication.views.create_custom_user_view import CreateCustomUserView


class CreateCustomUserViewTest(TestCase):
    """Test CreateCustomUserView view class.
    """
    def setUp(self):
        self.view = CreateCustomUserView()

    def test_init_with_ccuv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr_view_template(self):
        self.assertEqual(
            self.view.view_template,
            'authentication/create_custom_user.html'
        )
    def test_init_with_attr_post_nominal_view_name(self):
        self.assertEqual(
            self.view.post_view_name, 'authentication:login'
        )
