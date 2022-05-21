# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from authentication.views.update_custom_user_view import UpdateCustomUserView


class UpdateCustomUserViewTest(TestCase):

    def setUp(self):
        self.view = UpdateCustomUserView()

    def test_init_with_ecuv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr_nominal_template(self):
        self.assertEqual(
            self.view.view_template,
            'authentication/update_custom_user.html'
        )
        self.assertEqual(
            UpdateCustomUserView.login_url, '/authentication/login/'
        )
        self.assertEqual(UpdateCustomUserView.redirect_field_name, None)
