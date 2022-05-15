# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase

from chat.forms.collectivity_discussions_form import (
    CollectivityDiscussionsForm
)
from chat.views.collectivity_discussions_view import (
    CollectivityDiscussionsView
)


class CollectivityDiscussionsViewTest(TestCase):

    def setUp(self):
        self.view = CollectivityDiscussionsView()

    def test_init_with_overview_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertIsInstance(
            self.view.context['form'], CollectivityDiscussionsForm
        )
        self.assertIsNone(self.view.context['page_objects'])
        self.assertEqual(self.view.view_template, 'chat/discussions.html')
        self.assertEqual(
            CollectivityDiscussionsView.login_url, '/authentication/login/'
        )
        self.assertEqual(
            CollectivityDiscussionsView.redirect_field_name, None
        )
