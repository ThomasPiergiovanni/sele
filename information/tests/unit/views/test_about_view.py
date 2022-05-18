# pylint: disable=C0114,C0115,C0116,W0212
from django.test import TestCase

from information.views.about_view import AboutView


class TestAboutView(TestCase):

    def setUp(self):
        self.view = AboutView()

    def test_init_with_about_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template, 'information/about.html')
