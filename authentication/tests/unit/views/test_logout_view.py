# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from authentication.views.logout_view import LogoutView


class LogoutViewTest(TestCase):

    def setUp(self):
        self.view = LogoutView()

    def test_init_with_lv_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr_nominal_view_name(self):
        self.assertEqual(self.view.view_name, 'information:home')
