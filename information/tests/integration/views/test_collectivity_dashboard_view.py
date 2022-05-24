# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase
from django.urls import reverse

from authentication.models import CustomUser
from chat.models import Discussion
from information.tests.emulation.information_emulation import (
    InformationEmulation
)
from proposition.models import Proposition
from vote.models import Voting


class CollectivityDashboardViewTest(TestCase):

    def setUp(self):
        self.information_emulation = InformationEmulation()
        self.information_emulation.emulate_test_setup()

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
        self.assertTrue(response.context['custom_users_p_counts'][0])
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
            response.redirect_chain[0][0], reverse('authentication:login')
        )
