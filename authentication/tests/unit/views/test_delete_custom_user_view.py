# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from authentication.views.delete_custom_user_view import DeleteCustomUserView


class DeleteCustomUserViewTest(TestCase):

    def setUp(self):
        self.view = DeleteCustomUserView()

    def test_init_with_dcuv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(
            self.view.view_template, 'authentication/delete_custom_user.html'
        )
        self.assertEqual(
            DeleteCustomUserView.login_url, '/authentication/login/'
        )
        self.assertEqual(DeleteCustomUserView.redirect_field_name, None)
