# pylint: disable=C0116, W0212
"""Test home view module.
"""
from django.test import TestCase

from information.views.home_view import HomeView


class TestHomeView(TestCase):
    """Test home view class.
    """
    def setUp(self):
        self.view = HomeView()

    def test_init_with_deatile_voting_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'information/home.html')
        self.assertIsNone(self.view.context['mapbox_url'])
        self.assertIsNone(self.view.context['vector_layer'])
