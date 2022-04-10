"""Test update proposition view module.
"""
from django.test import TestCase

from proposition.views.update_proposition_view import UpdatePropositionView

class UpdatePropositionViewTest(TestCase):
    """Test UpdatePropositionView class.
    """
    def setUp(self):
        self.view = UpdatePropositionView()

    def test_init_with_update_proposition_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(
            self.view.post_view_name,'proposition:collectivity_propositions'
        )
        self.assertEqual(
            UpdatePropositionView.login_url , '/authentication/login/'
        )
        self.assertEqual(UpdatePropositionView.redirect_field_name, None)
        self.assertEqual(
            self.view.msg_post_success,
            "Le statut de la proposition a été mis-à-jour"
        )

