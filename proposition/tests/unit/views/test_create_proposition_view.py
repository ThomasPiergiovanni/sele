"""Test create proposition view module.
"""
from django.test import TestCase

# from proposition.forms.proposition_form import PropositionForm
# from proposition.views.create_proposition_view import PropositionView


# class CreatePropositionViewTest(TestCase):
#     """Test CreatePropsoitionView class.
#     """
#     def setUp(self):
#         self.view = PropositionView()

#     def test_init_with_create_proposition_instance(self):
#         self.assertTrue(self.view)

#     def test_init_with_attr(self):
#         self.assertEqual(
#             self.view.view_template,'proposition/create_proposition.html'
#         )
#         self.assertEqual(self.view.alternative_view_name, 'information:home')
#         self.assertEqual(self.view.post_view_name, 'proposition:collectivity_propositions')
#         self.assertIsInstance(self.view.context['form'], PropositionForm)