# pylint: disable=C0114,C0115,C0116
from django.test import TestCase


class LegalViewTest(TestCase):

    def test_get_with_nominal_scenario(self):
        response = self.client.get('/legal/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/legal.html')
