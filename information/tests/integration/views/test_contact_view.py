# pylint: disable=C0116
"""Test contact view module.
"""
from django.test import TestCase

class ContactViewTest(TestCase):
    """Test contact view class.
    """

    def setUp(self):
        pass

    def test_get_with_nominal_scenario(self):
        response = self.client.get('/contact/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/contact.html')
