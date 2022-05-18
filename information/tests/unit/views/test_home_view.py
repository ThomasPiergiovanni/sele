# pylint: disable=C0114,C0115,C0116,W0212
from django.test import TestCase

from information.views.home_view import HomeView


class TestHomeView(TestCase):

    def setUp(self):
        self.view = HomeView()

    def test_init_with_deatile_voting_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template, 'information/home.html')
        self.assertIsNone(self.view.context['mapbox_url'])
        self.assertIsNone(self.view.context['vector_layer'])
        self.assertIsNone(self.view.context['stats_data'])
        self.assertIsNone(self.view.context['all_p_counts'])
        self.assertIsNone(self.view.context['all_cu_counts'])
        self.assertIsNone(self.view.context['all_co_counts'])
        self.assertIsNone(self.view.context['all_v_counts'])
        self.assertIsNone(self.view.context['propositions'])
