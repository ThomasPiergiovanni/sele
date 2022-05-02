# pylint: disable=C0116
"""Test about view module.
"""
from django.test import TestCase

class AboutViewTest(TestCase):
    """Test about view class.
    """

    def setUp(self):
        pass

    def test_get_with_nominal_scenario(self):
        response = self.client.get('/about/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/about.html')
