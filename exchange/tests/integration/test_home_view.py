# pylint: disable=C0116
"""Test home view module.
"""
from django.test import TestCase

from exchange.forms.navbar_search_form import NavbarSearchForm


class HomeViewTest(TestCase):
    """Test home view class.
    """

    def test_get_with_status_code_200(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_get_with_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'exchange/home.html')

    def test_get_with_navbar_form(self):
        response = self.client.get('')
        self.assertIsInstance(
            response.context['navbar_search_form'], NavbarSearchForm
        )
