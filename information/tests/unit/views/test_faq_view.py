# pylint: disable=C0114,C0115,C0116,W0212
from django.test import TestCase

from information.views.faq_view import FaqView


class TestFaqView(TestCase):

    def setUp(self):
        self.view = FaqView()

    def test_init_with_faq_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template, 'information/faq.html')
        self.assertIsNone(self.view.context['questions'])
