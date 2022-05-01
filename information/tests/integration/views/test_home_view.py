# pylint: disable=C0116
"""Test home view module.
"""
from django.test import TestCase
from json import loads

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.tests.emulation.chat_emulation import ChatEmulation 
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)
from proposition.tests.emulation.proposition_emulation import PropositionEmulation
from vote.tests.emulation.vote_emulation import VoteEmulation


class HomeViewTest(TestCase):
    """Test home view class.
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
        response = self.client.get(
            '', follow=True
        )
        vector_layer = loads(response.context['vector_layer'])
        stats_data = loads(response.context['stats_data'])        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'information/home.html'
        )
        self.assertTrue(response.context['mapbox_url'])
        self.assertEqual(
            vector_layer['features'][0]
            ['properties']['name'], 'Bourg-la-Reine'
        )
        self.assertEqual(stats_data['cu_counts'][0], '0')
        self.assertEqual(response.context['all_p_counts'], 15)
        self.assertEqual(response.context['all_cu_counts'], 3)    
        self.assertEqual(response.context['all_co_counts'], 2)
        self.assertEqual(response.context['all_v_counts'], 3)
        self.assertEqual(response.context['propositions'][0].id , 17)

