"""Test collectivity dashboard view module.
"""
from django.test import TestCase
from django.urls import reverse


from authentication.models import CustomUser
from chat.models.discussion import Discussion
from proposition.models.proposition import Proposition
from vote.models.voting import Voting
from vote.models.vote import Vote

# from chat.forms.comment_form import CommentForm
# from chat.models.comment import Comment
# from chat.tests.emulation.chat_emulation import ChatEmulation
# from chat.models.discussion import Discussion
# from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)
from vote.tests.emulation.vote_emulation import (
   VoteEmulation
)

class CollectivityDashboardViewTest(TestCase):
    """Test CollectivityDashoardView class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.vote_emulation = VoteEmulation()

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
        self.assertEqual(response.context['collectivity_p_counts'], 15)
        self.assertEqual(response.context['collectivity_cu_counts'], 2)
        self.assertEqual(response.context['collectivity_d_counts'], 3)


    def test_get_with_nominal_scenario_with_voting(self):
        self.vote_emulation.emulate_voting()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/information/collectivity_dashboard/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'information/collectivity_dashboard.html'
        )
        self.assertIsInstance(response.context['voting_pag_obj'][0], Voting)
        self.assertEqual(response.context['collectivity_v_counts'], 2)

    def test_get_with_alternative_scenario(self):
        self.proposition_emulation.emulate_proposition()
        response = self.client.get(
            '/information/collectivity_dashboard/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )