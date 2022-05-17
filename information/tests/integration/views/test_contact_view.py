# pylint: disable=C0114,C0115,C0116
from django.test import TestCase


class ContactViewTest(TestCase):

    def test_get_with_nominal_scenario(self):
        response = self.client.get('/contact/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/contact.html')
