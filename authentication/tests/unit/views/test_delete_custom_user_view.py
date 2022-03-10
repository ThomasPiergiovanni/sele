"""Test delete custom user module.
"""
from django.test import TestCase

from authentication.views.delete_custom_user_view import DeleteCustomUserView


class DeleteCustomUserViewTest(TestCase):
    """Test DeleteCustomUserView class.
    """
    def setUp(self):
        self.view = DeleteCustomUserView()

    def test_init_with_dcuv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(
            self.view.view_template,'authentication/delete_custom_user.html'
        )
        self.assertEqual(
            self.view.alternative_view_name,'information:home'
        )
