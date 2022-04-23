"""Test collectivity dashboard view module.
"""
from django.test import TestCase

from information.views.collectivity_dashboard_view import (
    CollectivityDashboardView
)

class CollectivityDashboardViewTest(TestCase):
    """TestCollectivityDashboardView class.
    """
    def setUp(self):
        self.view = CollectivityDashboardView()

    def test_init_with_deatile_voting_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(
            self.view.view_template,'information/collectivity_dashboard.html'
        )
        self.assertEqual(
            CollectivityDashboardView.login_url , '/authentication/login/'
        )
        self.assertEqual(CollectivityDashboardView.redirect_field_name, None)
        self.assertIsNone(self.view.context['custom_user_pag_obj'])
        self.assertIsNone(self.view.context['custom_users_p_counts'])
        self.assertIsNone(self.view.context['proposition_pag_obj'])
        self.assertIsNone(self.view.context['discussion_pag_obj'])        
        self.assertIsNone(self.view.context['votation_pag_obj'])  
