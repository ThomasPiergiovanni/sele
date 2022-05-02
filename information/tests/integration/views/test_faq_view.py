# pylint: disable=C0116
"""Test faq view module.
"""
from django.test import TestCase

from information.tests.emulation.information_emulation import (
    InformationEmulation
)
from information.models.question import Question


class FaqViewTest(TestCase):
    """Test Faq view class.
    """

    def setUp(self):
        self.information_emulation = InformationEmulation()
        self.information_emulation.emulate_question()

    def test_get_with_nominal_scenario(self):
        response = self.client.get('/faq/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'information/faq.html')
        self.assertTrue(response.context['questions'])
        self.assertEqual(response.context['questions'][0].id, 1)
