"""Test login view module.
"""
from django.test import TestCase

from authentication.views.login_view import LoginView


class LoginViewTest(TestCase):
    """Test LoginView  class.
    """
    def setUp(self):
        self.view = LoginView()

    def test_init_with_lv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr_nominal_template(self):
        self.assertEqual(
            self.view.nominal_template,
            'authentication/login.html'
        )
    def test_init_with_attr_post_nominal_view_name(self):
        self.assertEqual(
            self.view.post_nominal_view_name,
            'information:home'
        )
