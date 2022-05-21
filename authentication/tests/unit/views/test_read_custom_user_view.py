# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from authentication.views.read_custom_user_view import ReadCustomUserView


class ReadCustomUserViewTest(TestCase):

    def setUp(self):
        self.view = ReadCustomUserView()

    def test_init_with_ecuv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr_view_template(self):
        self.assertEqual(
            self.view.view_template, 'authentication/read_custom_user.html'
        )
        self.assertEqual(
            ReadCustomUserView.login_url, '/authentication/login/'
        )
        self.assertEqual(ReadCustomUserView.redirect_field_name, None)
