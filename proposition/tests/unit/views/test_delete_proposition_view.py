# pylint: disable=C0114,C0115,C0116,E1101,W0212
from django.test import TestCase

from proposition.views.delete_proposition_view import DeletePropositionView


class DeletePropositionViewTest(TestCase):

    def setUp(self):
        self.view = DeletePropositionView()

    def test_init_with_create_proposition_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(
            self.view.view_template, 'proposition/delete_proposition.html'
        )
        self.assertEqual(
            self.view.alternative_one_view_name,
            'proposition:collectivity_propositions'
        )
        self.assertEqual(
            DeletePropositionView.login_url, '/authentication/login/'
        )
        self.assertEqual(DeletePropositionView.redirect_field_name, None)
        self.assertIsNone(self.view.context['proposition'])
        self.assertEqual(self.view.msg_post_success, "Suppression réussie")
        self.assertEqual(
            self.view.msg_not_owner,
            "Le créateur seulement peut supprimer la proposition"
        )
        self.assertEqual(
            self.view.mgs_post_no_delete,
            "Une proposition avec ce satut ne peut pas être supprimée"
        )
