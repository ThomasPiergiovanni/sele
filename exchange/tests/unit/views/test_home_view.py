# pylint: disable=C0116, W0212
"""Test home view module.
"""
from django.test import TestCase

from exchange.views.home_view import HomeView


class TestHomeView(TestCase):
    """Test home view class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.home_view = HomeView()

    def test_init__with_index_view(self):
        self.assertTrue(self.home_view)

    def test_init_with_attr_data_render(self):
        self.assertEqual(
            self.home_view.render,
            'exchange/home.html'
        )
