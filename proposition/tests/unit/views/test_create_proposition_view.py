# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase

from proposition.forms.proposition_form import PropositionForm
from proposition.views.create_proposition_view import CreatePropositionView


class CreatePropositionViewTest(TestCase):

    def setUp(self):
        self.view = CreatePropositionView()

    def test_init_with_create_proposition_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(
            self.view.view_template, 'proposition/create_proposition.html'
        )
        self.assertIsInstance(self.view.context['form'], PropositionForm)
        self.assertEqual(
            self.view.post_view_name,
            'proposition:collectivity_propositions'
        )
        self.assertEqual(
            CreatePropositionView.login_url, '/authentication/login/'
        )
