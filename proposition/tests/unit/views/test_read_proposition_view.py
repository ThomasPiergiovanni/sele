"""Test read proposition view module.
"""
from django.test import TestCase

from proposition.views.read_proposition_view import ReadPropositionView

class ReadPropositionViewTest(TestCase):
    """TestReadPropositionView class.
    """
    def setUp(self):
        self.view = ReadPropositionView()

    def test_init_with_read_proposition_view_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'proposition/read_proposition.html')
        self.assertEqual(
            ReadPropositionView.login_url , '/authentication/login/'
        )
        self.assertEqual(ReadPropositionView.redirect_field_name, None)
        self.assertIsNone(self.view.context['proposition'])
        self.assertIsNone(self.view.context['href'])
        self.assertIsNone(self.view.context['class'])
        self.assertIsNone(self.view.context['text'])
