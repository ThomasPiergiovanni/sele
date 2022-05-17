# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase


class AboutViewTest(TestCase):

    def test_get_with_nominal_scenario(self):
        response = self.client.get('/about/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/about.html')
