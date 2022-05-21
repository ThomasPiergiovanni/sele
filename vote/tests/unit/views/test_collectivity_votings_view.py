# pylint: disable=C0114,C0115,C0116,E1101
from django.test import TestCase

from vote.forms.collectivity_votings_form import CollectivityVotingsForm
from vote.views.collectivity_votings_view import CollectivityVotingsView


class CollectivityVotingsViewTest(TestCase):

    def setUp(self):
        self.view = CollectivityVotingsView()

    def test_init_with_overview_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertIsInstance(
            self.view.context['form'], CollectivityVotingsForm
        )
        self.assertIsNone(self.view.context['page_objects'])
        self.assertEqual(self.view.view_template, 'vote/votings.html')
        self.assertEqual(
            CollectivityVotingsView.login_url, '/authentication/login/'
        )
        self.assertEqual(
            CollectivityVotingsView.redirect_field_name, None
        )
