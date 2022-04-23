"""Test collectivity dashboard view module.
"""
from django.test import TestCase
from django.urls import reverse


from authentication.models import CustomUser
from chat.models.discussion import Discussion
from proposition.models.proposition import Proposition

# from chat.forms.comment_form import CommentForm
# from chat.models.comment import Comment
# from chat.tests.emulation.chat_emulation import ChatEmulation
# from chat.models.discussion import Discussion
# from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)

class CollectivityDashboardViewTest(TestCase):
    """Test CollectivityDashoardView class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_get_with_nominal_scenario(self):
        self.proposition_emulation.emulate_proposition()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/information/collectivity_dashboard/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'information/collectivity_dashboard.html'
        )
        self.assertIsInstance(
            response.context['custom_user_pag_obj'][0], CustomUser
        )
        self.assertEqual(response.context['custom_users_p_counts'][0]['id'], 1)
        self.assertIsInstance(
            response.context['proposition_pag_obj'][0], Proposition
        )
        self.assertIsInstance(
            response.context['discussion_pag_obj'][0], Discussion
        )


    def test_get_with_alternative_scenario(self):
        self.proposition_emulation.emulate_proposition()
        response = self.client.get(
            '/information/collectivity_dashboard/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )
