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
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.tests.emulation.chat_emulation import ChatEmulation 
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)
from proposition.tests.emulation.proposition_emulation import PropositionEmulation
from vote.tests.emulation.vote_emulation import (
   VoteEmulation
)

class CollectivityDashboardViewTest(TestCase):
    """Test CollectivityDashoardView class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.collectivity_emulation = CollectivityEmulation()
        self.collectivity_emulation.emulate_collectivity()
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_discussion()
        self.chat_emulation.emulate_comment()
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_proposition()
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_voting_method()
        self.vote_emulation.emulate_voting()
        self.vote_emulation.emulate_vote()

    def test_get_with_nominal_scenario(self):
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
        response = self.client.get(
            '/information/collectivity_dashboard/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )
