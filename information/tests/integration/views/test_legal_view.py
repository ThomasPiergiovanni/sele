# pylint: disable=C0116
"""Test legal view module.
"""
from django.test import TestCase

class LegalViewTest(TestCase):
    """Test legal view class.
    """

    def setUp(self):
        pass

    def test_get_with_nominal_scenario(self):
        response = self.client.get('/legal/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/legal.html')
